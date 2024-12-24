# controllers/experience_controller.py
import json
import requests
from src.models.certificate import CertificateFactory
from src.views.certificate_view import CertificateView
from utils import get_direct_download_link

class CertificateController:
    def __init__(self):
        self.certificates = []
        self.view = CertificateView()


    def load_certificates_from_file(self, google_drive_link):
        direct_link = get_direct_download_link(google_drive_link)
        response = requests.get(direct_link)
        
        if response.status_code == 200:
            data = response.json()
            self.load_certificates(data)
        else:
            raise Exception(f"Failed to download file from Google Drive. Status code: {response.status_code}")


    def load_certificates(self, data):
            for item in data:
                certificate = CertificateFactory.create_certificate(
                    title=item["title"],
                    issued_by=item["issued_by"],
                    date=item["date"],
                    pdf_path=item["pdf_path"],
                    logos=item["logos"]
                )
                self.certificates.append(certificate)
    def display_certificates(self):
        certificate_details = [cert.get_certificate_details() for cert in self.certificates]
        self.view.display_all_certificates(certificate_details)
