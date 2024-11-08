import gradio as gr
from components.metadata_enhancement import create_metadata_tab
from components.interactive_search import create_search_tab

def create_app():
    with gr.Blocks(title="视频元数据增强器：让视频内容发挥价值") as app:
        with gr.Tabs():
            with gr.Tab("元数据增强"):
                create_metadata_tab()
            
            with gr.Tab("交互式图文搜索"):
                create_search_tab()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.launch()
