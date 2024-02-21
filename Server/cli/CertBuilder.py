from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import datetime

# Generate a private key for the CA
ca_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Details about who we are. For a CA, this should be your information.
ca_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My CA Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, "My CA"),
])

# Our certificate will be valid for 10 years
valid_from = datetime.datetime.utcnow()
valid_to = valid_from + datetime.timedelta(days=3650)

# Create a self-signed CA certificate
ca_certificate = x509.CertificateBuilder().subject_name(
    ca_subject
).issuer_name(
    ca_subject
).public_key(
    ca_private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_to
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None), critical=True,
).sign(ca_private_key, hashes.SHA256())

# Serialize private key and certificate
ca_private_key_pem = ca_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
ca_cert_pem = ca_certificate.public_bytes(serialization.Encoding.PEM)

# Save the CA private key and certificate to files
with open("ca_private_key.pem", "wb") as f:
    f.write(ca_private_key_pem)

with open("ca_certificate.pem", "wb") as f:
    f.write(ca_cert_pem)
# Generate a private key for the server
server_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate a CSR for the server
server_csr = x509.CertificateSigningRequestBuilder().subject_name(
    x509.Name([
        # Adjust the details below according to your needs
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "My Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, "myserver.com"),
    ])
).sign(server_private_key, hashes.SHA256())

# Sign the CSR with the CA's private key
server_certificate = x509.CertificateBuilder().subject_name(
    server_csr.subject
).issuer_name(
    ca_certificate.subject
).public_key(
    server_csr.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    valid_from
).not_valid_after(
    valid_to
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName("myserver.com")]),
    critical=False,
).sign(ca_private_key, hashes.SHA256())

# Serialize server private key and certificate
server_private_key_pem = server_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
server_cert_pem = server_certificate.public_bytes(serialization.Encoding.PEM)

# Save the server private key and certificate to files
with open("server_private_key.pem", "wb") as f:
    f.write(server_private_key_pem)

with open("server_certificate.pem", "wb") as f:
    f.write(server_cert_pem)
# Print the server certificate
print(server_certificate.public_bytes(serialization.Encoding.PEM).decode('utf-8'))
# Print the server private key
print(server_private_key_pem.decode('utf-8'))
# Print the CA certificate
print(ca_cert_pem.decode('utf-8'))
# Print the CA private key
print(ca_private_key_pem.decode('utf-8'))
# Print the server certificate
print(server_cert_pem.decode('utf-8'))
# Print the server private key
print(server_private_key_pem.decode('utf-8'))
