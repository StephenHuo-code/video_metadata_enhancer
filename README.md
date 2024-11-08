# Video Metadata Enhancer (视频元数据增强器)

A powerful tool for enhancing video metadata and enabling interactive video content search.

[English](#features) | [中文](#功能特点)

## Features

- **Video Metadata Enhancement**
  - Support for BytePlus VOD video playback
  - Video space management and browsing
  - Manual and automatic video analysis
  - Screenshot capture and management
  - Metadata tagging and organization

- **Interactive Search**
  - Image-based video search
  - Interactive chat interface
  - High-aesthetic image filtering
  - Visual search results gallery

---

# 视频元数据增强器

一个用于增强视频元数据并支持交互式视频内容搜索的强大工具。

## 功能特点

- **视频元数据增强**
  - 支持 BytePlus VOD 视频播放
  - 视频空间管理和浏览
  - 手动和自动视频分析
  - 截图捕获和管理
  - 元数据标记和组织

- **交互式搜索**
  - 基于图像的视频搜索
  - 交互式聊天界面
  - 高美感图片筛选
  - 可视化搜索结果展示

## 环境要求

- Python 3.11+
- BytePlus SDK 凭证 (AK/SK)
- BytePlus VOD 服务访问权限

## 安装步骤

1. **克隆仓库：**

   ```shell
   git clone https://github.com/yourusername/video_metadata_enhancer.git
   cd video_metadata_enhancer
   ```

2. **创建虚拟环境并激活：**

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **安装依赖：**

   ```shell
   pip install -r requirements.txt
   ```

4. **设置环境变量：**

   确保设置 `BYTEPLUS_AK` 和 `BYTEPLUS_SK` 环境变量以进行认证。

   ```shell
   export BYTEPLUS_AK='your_access_key'
   export BYTEPLUS_SK='your_secret_key'
   ```

5. **运行应用程序：**

   ```shell
   python video_metadata_enhancer/app.py
   ```

   访问 `http://127.0.0.1:7865` 在浏览器中查看应用程序。

## 贡献

欢迎贡献！请 fork 本仓库并提交 pull request。

## 许可证

此项目采用 MIT 许可证。
