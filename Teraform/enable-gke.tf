resource "google_project_service" "gke_service" {
  project = var.project_id
  service = "container.googleapis.com"
}

resource "google_project_service" "compute_service" {
  project = var.project_id
  service = "compute.googleapis.com"
}
