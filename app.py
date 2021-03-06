import os
import sys
import time

# Set Timezone
time.strftime('%X %x %Z %w')
os.environ['TZ'] = "Atlantic/Reykjavik"
time.tzset()

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def root():
  day = int(time.strftime('%w')) # 0 for Sunday
  hr =  int(time.strftime('%H'))
  if day == 0 or day == 6:
    # print("Out of Office")
    return jsonify({"messages": [{"text": "Out of Office"}]})
  else:
    if hr >= 9 and hr <= 16:
      # print("Office Hour")
      return jsonify({"messages": [{"text": "Office Hour"}]})
    else:
      return jsonify({"messages": [{"text": "Out of Office"}]})

if __name__ == "__main__":
  # Debugging Disabled
  app.debug = False
  # Get the port number from environment
  app.port = int(os.environ.get("PORT", 5000))
  # Run the app
  app.run()
