# 🛡️ Core Security Principles – IBM Cybersecurity Fundamentals

This section introduces essential security principles used to **design, evaluate, and enforce** information security across systems and organizations. Mastery of these concepts is foundational for any cybersecurity role.

---

## 🧠 1. The CIA Triad

The **CIA Triad** is the core model for understanding information security:

| Principle       | Description                                      | Example                        |
|-----------------|--------------------------------------------------|--------------------------------|
| 🔒 Confidentiality | Ensure that only authorized parties access data | File encryption, MFA, ACLs     |
| 🧩 Integrity        | Maintain data accuracy and consistency          | Checksums, digital signatures  |
| 🕒 Availability     | Ensure systems/data are accessible when needed  | Redundancy, failover, backups  |

> 🔐 A breach of any element weakens the entire security posture.

---

## 🔍 2. Least Privilege

**Principle**: Users, programs, and systems should only have the **minimum access necessary** to perform their function.

- 🔧 Prevents privilege escalation
- 🔐 Limits damage in case of account compromise

✅ **Best Practices**:
- Use role-based access control (RBAC)
- Regularly review and revoke unused privileges

---

## 🏰 3. Defense in Depth

**Layered security** – deploy multiple overlapping controls to compensate for the failure of any one mechanism.

```plaintext
[Firewall] → [Antivirus] → [Host-based IDS] → [Access Control] → [User Training]
```

Each layer protects against different classes of threats.

## 🛡 Example:

Even if malware bypasses the firewall, endpoint antivirus may detect it.

## ⚖️ 4. Security vs Usability

| Design Focus | Strength       | Weakness                        |
| ------------ | -------------- | ------------------------------- |
| 🔐 Security  | Reduced risk   | Slower workflows, more friction |
| 🚀 Usability | Ease of access | May increase attack surface     |

⚠️ Security professionals must balance protection with business productivity.

## 📉 5. Risk Management

🔹 What is Risk?

Risk = Threat × Vulnerability × Impact

- Identify assets → threats → vulnerabilities → assess impact

## 🔸 Controls:

- Preventive (firewalls)

- Detective (IDS/monitoring)

- Corrective (patching, recovery)

✅ Use frameworks: NIST SP 800-30, ISO 27005

## 📌 6. Real-World Applications

| Principle           | Real Use Case                          |
| ------------------- | -------------------------------------- |
| Least Privilege     | Admin access restricted to IT team     |
| Defense in Depth    | Firewall + EDR + training              |
| Risk-Based Approach | Invest more protection on critical DBs |
| Confidentiality     | Encrypt emails with PGP                |

## 🧠 Pro Tips

- Start from a baseline security policy

- Apply Zero Trust assumptions by default

- Document access and audit trails

## 📚 References

- IBM SkillBuild – Cybersecurity Fundamentals

- NIST Cybersecurity Framework

- OWASP Secure Design Principles

- ISO/IEC 27001:2022 – Information Security Management
