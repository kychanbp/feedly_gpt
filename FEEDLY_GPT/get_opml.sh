sudo mkdir /output
sudo chmod 777 /output

echo "Enter Your Bearer Token"
read token
echo "Using Bearer Token: $token"
final_curl_command="curl 'https://cloud.feedly.com/v3/opml' -H 'Authorization: Bearer $token'"
echo "Final curl command: $final_curl_command"
eval $final_curl_command -o "feedly.opml"
