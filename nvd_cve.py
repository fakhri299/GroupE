import requests
from bs4 import BeautifulSoup


#NR-nvd(cve_id) scrapes data about cve-id from nvd website
def nvd(cve_id):
    link_nvd = f"https://nvd.nist.gov/vuln/detail/{cve_id}"
    response = requests.get(link_nvd)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        nvd_summary_raw = soup.find("p", {"data-testid": "vuln-description"})
        nvd_cvss_raw = soup.find("a", {"data-testid": "vuln-cvss3-panel-score"})
        nvd_vector_raw = soup.find("span", {"data-testid": "vuln-cvss3-nist-vector"})
        nvd_ref1_raw = soup.find("td", {"data-testid": "vuln-hyperlinks-link-0"})
        nvd_ref2_raw = soup.find("td", {"data-testid": "vuln-hyperlinks-link-1"})
    except Exception as e:
        print(f"Error while parsing NVD page: {e}")
        return None, None, None, None, None

    if not (nvd_summary_raw and nvd_cvss_raw and nvd_vector_raw and nvd_ref1_raw and nvd_ref2_raw):
        print("Incomplete or missing information for exploit.")
        return None, None, None, None, None

    nvd_summary = nvd_summary_raw.text.strip() if nvd_summary_raw else "Summary is not available"
    nvd_cvss = nvd_cvss_raw.text.strip() if nvd_cvss_raw else "CVSS not available"
    nvd_vector = nvd_vector_raw.text.strip() if nvd_vector_raw else "Vector not found"
    nvd_ref1 = nvd_ref1_raw.text.strip() if nvd_ref1_raw else "Reference not found"
    nvd_ref2 = nvd_ref2_raw.text.strip() if nvd_ref2_raw else "Reference not found"

    return nvd_summary, nvd_cvss, nvd_vector, nvd_ref1, nvd_ref2




# NR-mitre_exploit_db(cve_id) scrapes data about cve-id from mitre_exploit_db(cve_id) website
def mitre_exploit_db(cve_id):
    link_mitre = f"https://www.exploit-db.com/search?cve={cve_id}"
    response = requests.get(link_mitre)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        mitre_summary_raw = soup.find("td", {"colspan": "2"})
        mitre_cvss_raw = soup.find("selector_for_cvss")
        mitre_vector_raw = soup.find("selector_for_vector")
        mitre_ref1_raw = soup.find("selector_for_ref1")
        mitre_ref2_raw = soup.find("selector_for_ref2")
    except Exception as e:
        print(f"Error while parsing MITRE Exploit Database page: {e}")
        return None, None, None, None, None

    if not (mitre_summary_raw and mitre_cvss_raw and mitre_vector_raw and mitre_ref1_raw and mitre_ref2_raw):
        print("Incomplete or missing information for exploit.")
        return None, None, None, None, None

    mitre_summary = mitre_summary_raw.text.strip() if mitre_summary_raw else "Summary is not available"
    mitre_cvss = mitre_cvss_raw.text.strip() if mitre_cvss_raw else "CVSS not available"
    mitre_vector = mitre_vector_raw.text.strip() if mitre_vector_raw else "Vector not found"
    mitre_ref1 = mitre_ref1_raw.text.strip() if mitre_ref1_raw else "Reference not found"
    mitre_ref2 = mitre_ref2_raw.text.strip() if mitre_ref2_raw else "Reference not found"

    return mitre_summary, mitre_cvss, mitre_vector, mitre_ref1, mitre_ref2



