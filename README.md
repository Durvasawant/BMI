# BMI Calculator: DevOps Project

## Technologies
- HTML, CSS, JavaScript
- Git and GitHub
- GitHub Actions
- Docker and Docker Hub
- Kubernetes and Minikube
- Prometheus and Grafana
- Python and Streamlit

## Run HTML
Open index.html in your browser.

## Run with Docker
Replace YOUR-DOCKERHUB-USERNAME with your Docker Hub username
in k8s/deployment.yaml before deploying.

    docker build -t bmi-calculator .
    docker run --rm -p 8080:80 bmi-calculator

Open http://localhost:8080

## Run with Streamlit

    python -m pip install -r requirements.txt
    python -m streamlit run app.py

Open http://localhost:8501

## Kubernetes
Apply the deployment and service after building and publishing
your image to Docker Hub.

    kubectl apply -f k8s/deployment.yaml
    kubectl apply -f k8s/service.yaml

Install the Prometheus/Grafana stack before applying servicemonitor.yaml.
