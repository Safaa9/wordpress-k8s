from diagrams import Diagram, Cluster
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import MySQL
from diagrams.k8s.compute import Pod
from diagrams.k8s.network import Ingress, Service
from diagrams.k8s.storage import PV
from diagrams.onprem.client import User

with Diagram("WordPress on Kubernetes", show=True, direction="TB"):

    # External user
    user = User("External User\nBrowser")

    # Host OS layer
    with Cluster("Minikube- Host"):
        docker = Docker("Docker Runtime")

        # Minikube Cluster
        with Cluster("Minikube Cluster"):
            ingress = Ingress("NGINX Ingress")
            service = Service("ClusterIP Service")

            # WordPress Deployment
            with Cluster("WordPress Deployment"):
                wp_pod = Pod("WordPress Pod")
                wp_pv = PV("WordPress PV")

            # MariaDB StatefulSet
            with Cluster("MariaDB StatefulSet"):
                db_pod = Pod("MariaDB Pod")
                db_pv = PV("MariaDB PV")

    # Connections
    user >> ingress >> service >> wp_pod
    wp_pod >> db_pod
    wp_pod >> wp_pv
    db_pod >> db_pv
