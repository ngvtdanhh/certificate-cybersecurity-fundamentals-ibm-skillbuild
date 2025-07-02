# ⚠️ Common Cybersecurity Threats – IBM Cybersecurity Fundamentals

Understanding the threat landscape is essential for designing effective defenses. Below are common attack types every cybersecurity professional should recognize.

---

## 🦠 1. Malware

**Malicious Software**: Code designed to damage, disrupt, or gain unauthorized access.

| Type         | Description                       | Example                          |
|--------------|-----------------------------------|----------------------------------|
| Virus        | Replicates by attaching to files  | ILOVEYOU, Melissa                |
| Worm         | Spreads independently over network| Conficker, SQL Slammer           |
| Trojan       | Disguises as legitimate software  | Emotet                            |
| Ransomware   | Encrypts files, demands payment   | WannaCry, REvil                  |

> 🎯 Mitigation: AV software, backups, patching

---

## 📧 2. Phishing & Social Engineering

Tricks victims into giving sensitive info (e.g., passwords).

- Email spoofing, fake login pages
- BEC (Business Email Compromise)

🎯 Mitigation:
- Security awareness training  
- Email filters, MFA, domain verification (DMARC)

---

## 🔐 3. Credential Attacks

| Type              | Method                          |
|-------------------|----------------------------------|
| Brute Force       | Try all password combinations    |
| Dictionary Attack | Try common passwords             |
| Credential Stuffing | Use leaked credentials         |

🧠 Prevention:
- Use strong, unique passwords  
- Apply rate-limiting, MFA

---

## 🌐 4. Denial of Service (DoS/DDoS)

Flooding a service to make it unavailable.

- SYN flood, HTTP GET flood, DNS amplification

🛡 Mitigation:
- Rate limiting, firewalls, CDNs, anti-DDoS appliances

---

## 👤 5. Insider Threats

Employees or contractors abusing legitimate access.

- Unintentional (negligence)  
- Malicious (exfiltration, sabotage)

🛡 Controls:
- Audit logs  
- Least privilege  
- Behavioral monitoring

---

## 🧠 Pro Tips

- Check MITRE ATT&CK Matrix for real-world TTPs  
- Use threat intelligence feeds (MISP, OTX)

---

## 📚 References

- IBM SkillBuild – Cybersecurity Fundamentals  
- NIST SP 800-30 Risk Assessments  
- MITRE ATT&CK Framework  
- Verizon DBIR 2023 Report
