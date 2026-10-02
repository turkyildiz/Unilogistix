audit "file" "unilogistix-file" {
 description = "Fleet audit with HMAC-protected values"
 options {
  file_path = "/openbao/data/unilogistix-audit.jsonl"
  mode = "0600"
 }
}
