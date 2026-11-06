# Official Rules and Requirements :: Vultr Agent Rush Hackathon

> **Hackathon Name**: Vultr: Agent Rush Hackathon  
> **Hosts**: Lablab.ai ✕ Vultr  
> **Registration Fee**: $0.00 (Free Entry, $200 Vultr Cloud credits provided per builder)  
> **Competition Window**: November 03, 2026 - November 08, 2026  
> **Prize Pool**: $9,000+ USD  

---

## 1. Key Evaluation Pillars

1. **Autonomous Real-World Action Execution**:
   - The agent must execute real-world workflows (e.g. running shell scripts, interacting with headless browsers, querying external APIs, synthesizing reports).
   - Execution fidelity, error recovery, and autonomous planning are paramount.

2. **Isolated Sandbox Security Boundary**:
   - Destructive, untrusted, or exploratory agent operations must run inside an isolated sandbox (such as Docker disposable containers).
   - The sandbox must safely absorb and neutralize malicious attacks, filesystem wipes (`rm -rf / --no-preserve-root`), infinite recursion/loops, and high-resource exploits without affecting the host VM.

3. **Vultr Cloud & Vultr Serverless Inference Deployment**:
   - Backend services must run on Vultr Cloud compute infrastructure.
   - Core LLM reasoning must query Vultr Serverless Inference endpoints (`https://api.vultrinference.com/v1`) using OpenAI-compatible payload schemas.

4. **Production Web Dashboard**:
   - Deliver a live public Web UI (FastAPI/HTML/JS) providing full visual observability into agent thoughts, sandbox containment events, real-time command logs, and kill-switches.

5. **Hollywood 5-Act Demonstration Video**:
   - Deliver a high-definition presentation video featuring an explicit **Containment Moment** that visually captures the moment a destructive command is absorbed and neutralized inside the sandbox.

---

## 2. Hard Invariants & PHANToM GRID Standards

- **Rule 65 Compliance**: The Tri-Standard architecture (Typesetting Scroll, Hollywood Cinema, Official Match Requirements) is strictly enforced.
- **50.0 GB VRAM / Host RAM Ceiling**: Any run exceeding 50.0 GB triggers an immediate circuit breaker.
- **ZDR Purge 0.00 MB**: Zero-Drift-Residual memory scrubbing (0xAA -> 0x00) guarantees zero residue between task runs.
- **Language Purity**: 100% International English across all deliverables with zero Chinese characters.
