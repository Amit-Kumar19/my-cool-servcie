package authz

default allow = false

allow {
    input.method == "GET"
    input.role == "admin"
}

allow {
    input.method == "GET"
    input.role == "user"
}

allow {
    input.method == "POST"
    input.role == "admin"
}
