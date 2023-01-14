# Privacy Preserving Machine Learning

- client-app contains the Django project for handling client/users
- cloud-server contains the Django project for processing user data and running machine learning algorithms
- HElib and SEAL are homomorphic encryption libraries
- poc contains the simplified backend code that shows how the main thing works. Run the following steps to see how it works:
  ```bash
  cd poc
  bash runbook.sh
  ```

  Inside runbook.sh
  ```bash
  python3 client.py
  python3 model.py
  python3 server.py
  python3 results.py
  ```

  This will create the following files:
    - userkeys.json -- contains public and private key
    - data.json -- contains encrypted data and public key
    - answer.json -- contains encrypted ML result