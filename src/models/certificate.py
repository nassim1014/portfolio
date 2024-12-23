import streamlit as st
from abc import ABC, abstractmethod

class Certificate(ABC):
    @abstractmethod
    def get_certificate_details(self):
        pass

class Simple_certificate(Certificate):
    def __init__(self, title: str, issued_by: str, date: str, pdf_path: str, logos: list):
        self.title = title
        self.issued_by = issued_by
        self.date = date
        self.pdf_path = pdf_path  # Path to the PDF certificate
        self.logos = logos  # List of logos paths or URLs

    def get_certificate_details(self):
        return {
            "title": self.title,
            "issued_by": self.issued_by,
            "date": self.date,
            "pdf_path": self.pdf_path,
            "logos": self.logos
        }
    

class CertificateFactory:
    @staticmethod
    def create_certificate(certificate_type = "simple", **kwargs):
        if certificate_type == "simple":
            return Simple_certificate(kwargs["title"], kwargs["issued_by"], kwargs["date"], kwargs["pdf_path"], kwargs["logos"])
        else:
            raise ValueError("Invalid certificate type. Please choose 'Simple' or 'Pdf'.")