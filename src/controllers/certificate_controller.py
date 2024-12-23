# controllers/experience_controller.py
import json
from src.models.certificate import CertificateFactory
from src.views.certificate_view import CertificateView

class CertificateController:
    def __init__(self):
        self.certificates = []
        self.view = CertificateView()

    def load_certificates_from_file(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
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
