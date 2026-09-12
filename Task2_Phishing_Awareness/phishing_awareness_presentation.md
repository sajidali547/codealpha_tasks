@'
# Phishing Awareness Training
## CodeAlpha Cyber Security Internship - Task 2

---

## Slide 1: Title
# Phishing Awareness Training
### Protecting Yourself from Social Engineering Attacks
Presented by: Your Name

---

## Slide 2: What is Phishing?
Phishing is a cyberattack where attackers impersonate legitimate entities to steal sensitive information.

### Key Statistics
- 3.4 billion phishing emails sent daily
- 90% of data breaches start with phishing
- $17,700 lost every minute to phishing
- 1 in 4 organizations experience phishing attacks

---

## Slide 3: Types of Phishing
1. Email Phishing - Mass emails impersonating trusted brands
2. Spear Phishing - Targeted attacks on specific individuals
3. Whaling - Attacks on executives
4. Smishing - Phishing via SMS
5. Vishing - Voice phishing via phone
6. Clone Phishing - Copying legitimate emails with malicious links

---

## Slide 4: Recognizing Phishing Emails

### Red Flags
Sender:
- Misspelled domains (amaz0n.com)
- Generic greetings (Dear Customer)
- Unusual sender addresses

Content:
- Urgency (Act now!)
- Threats (Account will be closed)
- Requests for sensitive info
- Poor grammar

Links:
- Hover to see actual URL
- Mismatched display vs actual link
- Shortened URLs

Attachments:
- Unexpected attachments
- Dangerous file types (.exe, .scr, .js)

---

## Slide 5: Fake Website Indicators
1. Check URL spelling and HTTPS padlock
2. Look for poor design / broken links
3. Requests for unnecessary info
4. No contact information

---

## Slide 6: Social Engineering Tactics

| Tactic | Example |
|--------|---------|
| Authority | IT Dept needs your password |
| Urgency | Verify within 24 hours |
| Fear | Account will be suspended |
| Curiosity | See who viewed your profile |
| Reciprocity | Free gift card for survey |
| Social Proof | Join 10,000 users |

---

## Slide 7: Real-World Case Studies
- Google/Facebook (2013-2015): $100M loss via fake invoices
- Twitter Bitcoin Scam (2020): $118K loss via compromised accounts
- Ubiquiti Networks (2015): $46.7M loss via CEO fraud

---

## Slide 8: Best Practices

DO:
- Verify sender email addresses
- Hover over links before clicking
- Use multi-factor authentication
- Keep software updated
- Report suspicious emails

DON'T:
- Click links in unexpected emails
- Download unexpected attachments
- Share passwords via email
- Reuse passwords

---

## Slide 9: SOC Analyst Phishing Triage

Step-by-Step Email Analysis:
1. Check Sender - Display name vs actual address, Reply-To mismatch
2. Analyze Headers - SPF, DKIM, DMARC results, Received chain
3. Extract IOCs - URLs (VirusTotal, URLScan), attachments (hash), sender IP
4. Verdict - Malicious / Suspicious / Clean
5. Action - Escalate or close with notes

---

## Slide 10: Interactive Quiz

Q1: Email from Apple Support says account locked, click link to verify. What do you do?
- A) Click link  B) Reply with password  C) Navigate to Apple.com directly  D) Forward to friends
Answer: C

Q2: CEO emails urgently asking to wire $50,000 to new vendor. What do you do?
- A) Wire immediately  B) Call CEO to verify  C) Reply for details  D) Forward to accounting
Answer: B

Q3: Which URL is likely phishing?
- A) https://www.paypal.com/login
- B) https://www.paypa1.com/login
- C) https://www.paypal.com/security
- D) https://login.paypal.com
Answer: B (note the 1 instead of l)

---

## Slide 11: Reporting Phishing
- Internal: security@company.com, IT helpdesk
- FTC: reportfraud.ftc.gov
- APWG: reportphishing@apwg.org
- Google: reportphishing@google.com

---

## Slide 12: Summary
1. Think Before You Click
2. Verify the Sender
3. Check the URL
4. Enable 2FA
5. Report Suspicious Activity

Security is not a product, but a process. - Bruce Schneier

---

## Slide 13: Thank You
Contact: hafizsajidali547@gmail.com
'@ | Out-File -FilePath phishing_awareness_presentation.md -Encoding utf8