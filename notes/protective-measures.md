# 🔐 Protective Measures – IBM Cybersecurity Fundamentals

Effective cyber defense requires multiple tools and best practices. This section outlines **essential protective controls** across layers.

---

## 🔥 1. Firewalls

Filters traffic based on IP, port, or protocol.

- Types: Network, Host-based, Web Application Firewall (WAF)
- Stateful vs Stateless inspection

🛡 Use Cases:
- Block inbound port 22 (SSH)
- Allow HTTP(S) only to web servers

---

## 🧬 2. Antivirus & EDR

| Tool      | Function                                     |
|-----------|----------------------------------------------|
| Antivirus | Signature-based malware detection            |
| EDR       | Behavioral & forensic analysis post-infection|

✅ Best Practice: Combine AV with **Endpoint Detection & Response (EDR)**

---

## 🛡 3. Authentication & MFA

**Authentication types**:

- Something you know: password  
- Something you have: token, OTP  
- Something you are: fingerprint, face

🔐 Use MFA (Multi-Factor Authentication) to prevent credential-based attacks.

---

## 💾 4. Data Backups

| Type        | Frequency        | Notes                         |
|-------------|------------------|-------------------------------|
| Full        | Weekly           | All data                      |
| Incremental| Daily            | Only changed data             |
| Snapshot    | Every hour       | Fast rollback (VMs/databases) |

> 📦 Test restore procedures regularly!

---

## 🧑‍💻 5. Patching & Updates

- Apply OS and app patches to fix known vulnerabilities
- Use WSUS, SCCM, or centralized patch managers

🛠 Example: Patch for CVE-2021-44228 (Log4Shell)

---

## 📌 Security Policies

- Acceptable Use Policy (AUP)  
- Password Policy  
- Incident Response Plan

---

## 🧠 Pro Tips

- Use CIS Benchmarks for hardening  
- Automate configuration with Ansible/Chef  
- Use VPNs for remote access

---

## 📚 References

- IBM SkillBuild  
- OWASP Top 10  
- CIS Controls v8  
- NIST SP 800-53 – Security Controls
