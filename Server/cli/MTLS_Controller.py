import ssl
from CertBuilder import CertBuilder
from MTLS_Server import MTLS_Server
class MTLS_Controller:

    def __init__(self):
        self.command_options = {
            "MTLS": {"CA_CERT": None, "SERVER_CERT": None, "SERVER_KEY": None}
        }


    def start_mtls_server(self, host: str, port_str: str):
        """Starts the mTLS server with the given host and port."""
        try:
            port = int(port_str)
            mtls_options = self.command_options["MTLS"]
            mtls_server = MTLS_Server(mtls_options["CA_CERT"], mtls_options["SERVER_CERT"], mtls_options["SERVER_KEY"])
            mtls_server.start_server(host, port)
        except ValueError:
            print("Invalid port number.")
    def set_mtls_options(self, ca_cert: str, server_cert: str, server_key: str):
        """Sets the mTLS options."""
        self.command_options["MTLS"]["CA_CERT"] = ca_cert
        self.command_options["MTLS"]["SERVER_CERT"] = server_cert
        self.command_options["MTLS"]["SERVER_KEY"] = server_key
        print("mTLS options set.")
    def generate_mtls_certificates(self):
        print("Generating mTLS certificates...")
        ca_country = input("CA Country: ") 
        ca_state = input("CA State: ")
        ca_locality = input("CA Locality: ")
        ca_org = input("CA Organization: ")
        ca_common_name = input("CA Common Name: ")
        server_common_name = input("Server Common Name: ")
        validity_years = int(input("Certificate Validity (years): "))

        ca_cert_builder = CertBuilder(ca_country, ca_state, ca_locality, ca_org, ca_common_name, server_common_name, validity_years)

        ca_cert_builder.generate_ca_private_key()
        ca_cert_builder.generate_ca_certificate()
        ca_cert_builder.generate_server_private_key()
        ca_cert_builder.generate_server_certificate()

        ca_cert_builder.save_certificates()
        print("mTLS certificates generated and saved.")

    