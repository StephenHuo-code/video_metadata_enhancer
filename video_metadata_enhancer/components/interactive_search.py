import gradio as gr

def create_search_tab():
    with gr.Row():
        with gr.Column(scale=1):
            # Image upload area
            image_input = gr.Image(label="上传图片")
            
            # High aesthetic image options
            aesthetic_options = gr.CheckboxGroup(
                choices=["选项1", "选项2"], 
                label="高美感图片选项"
            )
            
            # Interactive chat
            chatbot = gr.Chatbot(label="交互式对话")
            msg_input = gr.Textbox(label="输入消息")
            send_btn = gr.Button("发送")
        
        with gr.Column(scale=1):
            # Search results
            video_results = gr.Gallery(label="搜索结果")
