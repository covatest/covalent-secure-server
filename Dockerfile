# core docker file to sandbox model training
FROM python:2.7

RUN pip install -U scikit-learn==0.19.2 numpy==1.14.5 scipy==1.1.0 pandas==0.23.3 requests==2.19.1 pynacl==1.2.1

ADD ./covalent-secure-models/ ./

CMD ["python", "./cova_secure_model_main.py"]