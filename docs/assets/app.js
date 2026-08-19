const Atlas = (() => {
  const TYPES = {
    question: "Research question", claim: "Claim", study: "Study", tool: "Tool or criteria",
    hypothesis: "Hypothesis", cohort: "Cohort", diagnostic_profile: "Diagnostic profile",
    case: "Worked case", source: "Source", topic: "Coverage topic"
  };
  const FIELD_GROUPS = {
    question: [
      ["What we know", ["current_answer"]], ["What is missing", ["critical_missing_piece"]],
      ["A study that could decide it", ["decisive_design"]],
      ["Scope", ["population","index_or_exposure","comparator","reference_standard","outcome","timing","setting"]],
      ["Evidence connections", ["claim_ids","study_ids","last_searched"]]
    ],
    claim: [
      ["What the evidence supports", ["interpretation_supported"]], ["What it does not establish", ["not_established"]],
      ["Why uncertainty remains", ["key_limitation"]], ["A decisive test", ["decisive_test"]],
      ["Evidence appraisal", ["confidence","directness","bias_control","consistency","precision","transportability","status","reviewed_on"]]
    ],
    study: [
      ["Finding", ["key_result"]], ["Major limitations", ["major_limitations"]],
      ["Who and where", ["design","population","n","setting"]],
      ["What was compared", ["index_test_or_exposure","reference_standard","outcome"]],
      ["Appraisal", ["appraisal_framework","provisional_bias","applicability","extraction_status","ref_id","reviewed_on"]]
    ],
    diagnostic_profile: [
      ["Bottom line", ["evidence_grade","main_failure_mode","next_validation"]],
      ["Validation chain", ["technical_validity","biological_validity","diagnostic_accuracy","prognostic_validity","incremental_value","transportability","clinical_utility"]],
      ["Context and sources", ["tool_id","context","key_refs"]]
    ],
    source: [
      ["Citation", ["authors_or_group","year","source","doi","pmid","pmcid","doi_or_url"]],
      ["Why it is here", ["evidence_type","topic","priority","archive_note"]],
      ["Archive status", ["metadata_status","reviewed_on"]]
    ],
    topic: [
      ["Coverage status", ["depth_status","current_module","priority"]],
      ["What remains", ["gap","next_action"]],
      ["Classification and sources", ["domain","kind","core_sources"]]
    ]
  };
  const esc = (value = "") => String(value).replace(/[&<>'"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[c]));
  const human = value => TYPES[value] || String(value || "").replaceAll("_", " ");
  const statusClass = value => { const t=String(value||"").toLowerCase(); return t.includes("critical")?"gap":t.includes("low")?"gap":t.includes("emerging")?"emerging":t.includes("moderate")?"emerging":t.includes("bounded")?"bounded":""; };
  const badge = (value, extra = "") => value ? `<span class="badge ${statusClass(value)} ${extra}">${esc(human(value))}</span>` : "";

  function shell(active = "", base = "") {
    const nav = [["learn.html","Learn","learn"],["coverage.html","Coverage","coverage"],["workbench.html","Criteria & tools","workbench"],["explore.html","Evidence library","explore"],["about.html","About","about"]];
    document.querySelector("#site-header").innerHTML = `<a class="skip-link" href="#main">Skip to content</a><header class="site-header"><div class="nav-wrap"><a class="brand" href="${base}index.html"><span class="brand-mark">cSVD</span><span class="brand-copy"><strong>Evidence Atlas</strong><small>Learn · reason · investigate</small></span></a><button class="nav-toggle" type="button" aria-label="Open navigation">Menu</button><nav class="site-nav" aria-label="Primary">${nav.map(([href,label,key])=>`<a href="${base}${href}" ${key===active?'aria-current="page"':''}>${label}</a>`).join("")}</nav></div></header>`;
    document.querySelector(".nav-toggle")?.addEventListener("click",()=>document.querySelector(".site-nav").classList.toggle("open"));
    document.querySelector("#site-footer").innerHTML = `<footer class="site-footer"><div class="container footer-grid"><div><strong>cSVD Evidence Atlas <span class="version">v0.6</span></strong><p class="fine">A web-native field guide and evidence workspace for CAA, brain arteriolosclerosis, and the wider small-vessel disease spectrum.</p></div><div><strong>Use responsibly</strong><p class="fine">Research and education only. No patient data. Findings are not diagnoses or treatment recommendations.</p></div><div><strong>Project</strong><p class="fine"><a href="https://github.com/kingkhalid310/cerebral-small-vessel-disease-atlas">GitHub repository</a><br><a href="${base}about.html#citation">Citation and methods</a></p></div></div></footer>`;
  }
  async function catalog(base="") { const response=await fetch(`${base}data/catalog.json`); if(!response.ok) throw new Error("The evidence catalog could not be loaded."); return response.json(); }
  function linkify(value, recordsById) {
    let output=esc(value); const ids=[...new Set(String(value).match(/\b(?:TOP|Q|C|S|T|H|COH|DP|UC|R)\d{3}\b/g)||[])];
    ids.sort((a,b)=>b.length-a.length).forEach(id=>{if(recordsById.has(id)) output=output.replaceAll(id,`<a href="record.html?id=${encodeURIComponent(id)}">${id}</a>`)});
    output=output.replace(/(https?:\/\/[^\s<]+)/g,'<a href="$1" rel="noopener">Open source ↗</a>'); return output;
  }
  function groupedFields(record, byId) {
    const map=new Map(record.fields.map(f=>[f.key,f])); const groups=FIELD_GROUPS[record.type]||[["Record details",record.fields.map(f=>f.key)]]; const used=new Set();
    const render=(title,keys)=>{const items=keys.filter(k=>map.has(k)).map(k=>{used.add(k);const f=map.get(k);return `<div class="evidence-field"><dt>${esc(f.label)}</dt><dd>${linkify(f.value,byId)}</dd></div>`}).join(""); return items?`<section class="evidence-section"><h2>${esc(title)}</h2><dl>${items}</dl></section>`:""};
    let html=groups.map(([title,keys])=>render(title,keys)).join(""); const remainder=record.fields.filter(f=>!used.has(f.key)&&!["question_id","claim_id","study_id","tool_id","profile_id","ref_id","name","title","question","claim","short_name"].includes(f.key));
    if(remainder.length) html+=render("Additional record details",remainder.map(f=>f.key)); return html;
  }
  function progress() {
    const button=document.querySelector("[data-progress]"); if(!button)return; const key=`csvd-complete-${button.dataset.progress}`;
    const update=()=>{const complete=localStorage.getItem(key)==="1"; button.textContent=complete?"✓ Completed":"Mark complete";button.classList.toggle("complete",complete)};
    button.addEventListener("click",()=>{localStorage.setItem(key,localStorage.getItem(key)==="1"?"0":"1");update()}); update();
  }
  return {TYPES,esc,human,badge,shell,catalog,linkify,groupedFields,progress};
})();
