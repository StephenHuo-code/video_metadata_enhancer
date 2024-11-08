import gradio as gr
from urllib.parse import urlparse
import yt_dlp  # 用于下载YouTube视频
import os
from utils.byteplus_sdk_function import get_vid_list, get_video_play_info

def load_video_from_vid(vid):
    """
    根据VID加载视频
    """
    if not vid:
        return None
    
    try:
        play_info = get_video_play_info(vid)
        if play_info and play_info.Result.PlayInfoList:
            # 获取第一个可用的播放地址
            video_url = play_info.Result.PlayInfoList[0].MainPlayUrl
            return video_url
    except Exception as e:
        gr.Warning(f"加载视频失败: {str(e)}")
        return None

def load_video_list(space_name):
    """
    加载视频空间中的视频列表
    """
    if not space_name:
        gr.Warning("请输入视频空间名称")
        return gr.Dropdown(choices=[], value=None), None
    
    vid_list = get_vid_list(space_name)
    if not vid_list:
        gr.Warning("获取视频列表失败，请检查认证信息和空间名称是否正确")
        return gr.Dropdown(choices=[], value=None), None
        
    # 创建新的选项列表
    choices = [f"{item['Title']} ({item['VID']})" for item in vid_list]
    # 返回更新后的下拉框
    return gr.Dropdown(choices=choices, value=None), None

def create_metadata_tab():
    with gr.Row():
        # Left Column
        with gr.Column(scale=1):
            # 将视频链接改为视频空间输入
            space_name = gr.Textbox(label="视频空间名称")
            video_selector = gr.Dropdown(
                choices=[], 
                label="选择视频", 
                interactive=True,
                value=None,
                allow_custom_value=True
            )
            play_button = gr.Button("开始播放")
            video_player = gr.Video()
            
            # Manual Analysis Section
            gr.Markdown("### 手动分析")
            manual_model = gr.Dropdown(choices=["模型1", "模型2"], label="选择模型")
            manual_analyze_btn = gr.Button("开始分析")
            
            # Auto Analysis Section
            gr.Markdown("### 自动分析")
            auto_model = gr.Dropdown(choices=["模型1", "模型2"], label="选择模型")
            analysis_time = gr.Slider(minimum=1, maximum=60, label="分析时间(秒)")
            auto_analyze_btn = gr.Button("开始分析")
        
        # Right Column
        with gr.Column(scale=1):
            video_name = gr.Textbox(label="视频名称")
            video_id = gr.Textbox(label="视频ID")
            video_description = gr.TextArea(label="视频描述")
            tags = gr.CheckboxGroup(choices=["标签1", "标签2"], label="标签选择")
            image_gallery = gr.Gallery(label="视频截图")
    
    # 绑定事件处理函数
    space_name.submit(
        fn=load_video_list,
        inputs=[space_name],
        outputs=[video_selector, video_player]
    )
    
    def play_selected_video(selected_video):
        if not selected_video:
            return None
        # 从选项中提取VID (格式: "Title (VID)")
        vid = selected_video.split("(")[-1].strip(")")
        print(f"Selected video ID: {vid}")
        return load_video_from_vid(vid)
    
    play_button.click(
        fn=play_selected_video,
        inputs=[video_selector],
        outputs=[video_player]
    )
