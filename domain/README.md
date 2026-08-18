# Custom-domain activation

The prepared address is `csvd.medics-global.com`. It is intentionally not activated by this release.

## When ready

1. Publish the repository and enable GitHub Pages from the `main` branch `/docs` folder.
2. At the DNS provider for `medics-global.com`, create a `CNAME` record:
   - Host/name: `csvd`
   - Target/value: `kingkhalid310.github.io`
3. Copy `domain/CNAME.example` to `docs/CNAME` and commit it.
4. In GitHub Pages settings, set the custom domain to `csvd.medics-global.com`.
5. Wait for DNS and certificate issuance, then enable **Enforce HTTPS**.
6. Verify both the GitHub Pages address and the custom domain before announcing launch.

Do not change apex-domain or email-related DNS records for this subdomain deployment.
