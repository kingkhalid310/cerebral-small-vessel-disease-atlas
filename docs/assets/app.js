const Atlas = (() => {
  const TYPES = {
    question: "Research question",
    claim: "Claim",
    study: "Study",
    tool: "Tool or criteria",
    hypothesis: "Hypothesis",
    cohort: "Cohort",
    diagnostic_profile: "Diagnostic profile",
    case: "Worked case",
    source: "Source"
  };

  const esc = (value = "") => String(value).replace(/[&<>'"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;","'":"&#39;",'"':"&quot;"}[c]));
  const human = value => TYPES[value] || String(value || "").replaceAll("_", " ");
  const statusClass = value => {
    const text = String(value || "").toLowerCase();
    if (text.includes("critical")) return "gap";
    if (text.includes("emerging")) return "emerging";
    if (text.includes("bounded")) return "bounded";
    return "";
  };
  const badge = (value, extra = "") => value ? `<span class="badge ${statusClass(value)} ${extra}">${esc(human(value))}</span>` : "";

  function shell(active = "") {
    const nav = [["index.html","Home","home"],["learn.html","Learn","learn"],["explore.html","Explore","explore"],["methodology.html","Methods","methods"],["about.html","About","about"]];
    document.querySelector("#site-header").innerHTML = `
      <a class="skip-link" href="#main">Skip to content</a>
      <header class="site-header"><div class="nav-wrap">
        <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true">SV</span><span class="brand-copy"><strong>cSVD Evidence Atlas</strong><small>CAA · arteriolosclerosis · mixed disease</small></span></a>
        <nav class="site-nav" aria-label="Primary">${nav.map(([href,label,key]) => `<a href="${href}" ${key===active?'aria-current="page"':''}>${label}</a>`).join("")}</nav>
      </div></header>`;
    document.querySelector("#site-footer").innerHTML = `
      <footer class="site-footer"><div class="container footer-grid">
        <div><strong>Cerebral Small Vessel Disease Evidence Atlas</strong><p class="fine">A question-driven research and educational resource. v0.4.</p></div>
        <div><strong>Boundaries</strong><p class="fine">Not medical advice. No patient data. No autonomous diagnosis.</p></div>
        <div><strong>Repository</strong><p class="fine"><a href="https://github.com/kingkhalid310/cerebral-small-vessel-disease-atlas">View source</a><br><a href="about.html#citation">Citation and reuse</a></p></div>
      </div></footer>`;
  }

  async function catalog() {
    const response = await fetch("data/catalog.json");
    if (!response.ok) throw new Error("The evidence catalog could not be loaded.");
    return response.json();
  }

  function linkify(value, recordsById) {
    let html = esc(value);
    const ids = [...new Set(String(value).match(/\b(?:Q|C|S|T|H|COH|DP|UC|R)\d{3}\b/g) || [])];
    ids.sort((a,b) => b.length - a.length).forEach(id => {
      if (recordsById.has(id)) html = html.replaceAll(id, `<a href="record.html?id=${encodeURIComponent(id)}">${id}</a>`);
    });
    html = html.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" rel="noopener">$1</a>');
    return html;
  }

  return { TYPES, esc, human, badge, shell, catalog, linkify };
})();
