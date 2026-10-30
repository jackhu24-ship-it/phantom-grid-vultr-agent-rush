# PHANToM GRID :: Vultr Agent Rush Hackathon

> **Tournament ID**: Competition 20  
> **Platform**: Lablab.ai (Vultr Co-Sponsored Hackathon)  
> **Track**: Sandboxed Real-World Agents & Autonomous Execution  
> **Architecture Sovereign**: Supreme Commander Jack Hu & Commander Xiaomi  
> **Engineering Vanguard**: Office 1 Pioneer Xiao-Ke & Office 3 Commander Xiao-Ma  

---

## 1. Overview & Operational Mandate

PHANToM GRID for the Vultr Agent Rush Hackathon introduces an enterprise-grade autonomous agent execution architecture running on Vultr Cloud compute and querying Vultr Serverless Inference (`https://api.vultrinference.com/v1`). 

### Core Pillars
1. **Isolated Sandbox Boundary**: Disposable throwaway container execution environment absorbing destructive bash commands (`rm -rf / --no-preserve-root`, fork bombs, infinite loops) and malicious headless browser flows without contaminating host or host cloud instances.
2. **Vultr Cloud Native Backend**: FastAPI/FastMCP orchestrator deployed on Vultr VM communicating with Vultr Serverless Inference using OpenAI-compatible APIs.
3. **Cyberpunk Dark Mode Web Dashboard**: Full-featured single-page web console with real-time telemetry, execution timeline, and containment kill-switch.
4. **ASIL-D Zero-Drift & ZDR Purge**: Mathematical resource defense with 50.0 GB VRAM circuit breaker and 0.00 MB Zero Drift Residual memory cleanup.

---

## 2. Directory Structure (10 Standard Drawers)

- `01_Specs`: White paper, mathematical formulations, four pure Mermaid diagrams, and resource matrix CSV.
- `02_SourceCode`: Full FastAPI backend, FastMCP bridge, containment runner, and runner state machine.
- `03_CoverImage_16x9`: Broadcast 16:9 full-bleed cover image and SVG generator.
- `04_Slides_PDF`: 10-page presentation deck compiled to broadcast vector PDF.
- `05_DemoVideo_1440P`: Hollywood 5-act demo video script and rendered 1440P MP4.
- `06_Deploy_and_Sandbox`: Vultr Cloud-Init automation scripts and deployment validation suite.
- `07_SubmissionPackage`: Official submission package copy with reproducible execution instructions.
- `08_AuditReceipts`: Immutable WORM audit receipt and verification tests.
- `09_ChaosReports`: 1,500-cycle chaos containment stress report and tests.
- `10_Releases`: Production release zip packager and manifest validation.

---

## 3. Quickstart & Verification

```bash
# Run all drawer gate tests
python run_all_drawers_tests.py

# Run tournament compliance audit
python test_tournament_compliance_gate.py
```
