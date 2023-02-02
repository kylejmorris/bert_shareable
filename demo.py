import banana_dev as banana

model_inputs = {
  "prompt": "Paris is the [MASK] of France."
}

api_key = "{YOUR_API_KEY}"
model_key = "{YOUR_MODEL_KEY}"

# Run the model
out = banana.run(api_key, model_key, model_inputs)

print(out) # show the output


