import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()

# URL: https://gradio.app/guides/creating-plots
# To run the app, use the following commands in your terminal:
# python -m creatingplot.py