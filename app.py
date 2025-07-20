
from flask import Flask, request, jsonify, render_template
from supabase import create_client, Client
app = Flask(__name__)

url: str = "https://ltsuvxczpjfoldcykhop.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx0c3V2eGN6cGpmb2xkY3lraG9wIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Mjk0ODM2MiwiZXhwIjoyMDY4NTI0MzYyfQ.vQjR-vPAW43uW-Cns4HXvOoZhnWVmpkQV-wR6jWEwhs"
supabase: Client = create_client(url, key)
@app.route('/', methods=['POST',"GET"])
def process_data():
    count_response = supabase.table("data").select("*", count="exact").execute()
    # response = supabase.table('data').select("*").limit(10).execute()
    start = count_response.count
    last_seen_id = 20
    response = (
    supabase
    .table("data")
    .select("*")
    .lt("id", last_seen_id)
    .order("id", desc=True)
    .limit(10)
    .execute()
)
    # response = (
    # supabase
    # .table("data")
    # .select("*")
    # .order("id", desc=True)
  #   .range(start -9, start)
  #   .execute()
  # )

    return render_template('home.html', data=response.data, total_count=count_response.count)

@app.route('/data', methods=['POST',"GET"])
def data():
    last_seen_id = 20
    response = (
    supabase
    .table("data")
    .select("*")
    .lt("id", 30)
    .order("id", desc=True)
    .limit(10)
    .execute()
)
    return jsonify(response.data)
if __name__ == '__main__':
    app.run(debug=True)
