import os
from byteplus_sdk.vod.VodService import VodService
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodGetMediaListRequest
from byteplus_sdk.vod.models.request.request_vod_pb2 import VodGetPlayInfoRequest

def get_video_play_info(vid: str):
    """
    获取视频播放信息
    Args:
        vid: 视频ID
    Returns:
        resp: 视频播放信息响应对象
    """
    vod_service = VodService()
    
    # 设置认证信息
    ak = os.getenv('BYTEPLUS_AK')
    sk = os.getenv('BYTEPLUS_SK')
    if ak and sk:
        vod_service.set_ak(ak)
        vod_service.set_sk(sk)
    
    try:
        req = VodGetPlayInfoRequest()
        req.Vid = vid
        req.Ssl = '0'
        resp = vod_service.get_play_info(req)
        
        if resp.ResponseMetadata.Error.Code == '':
            return resp
        else:
            print(f"Error: {resp.ResponseMetadata.Error}")
            return None
            
    except Exception as e:
        print(f"Failed to get video info: {str(e)}")
        return None
    

def get_vid_list(space_name: str) -> list:
    """
    从指定space获取所有视频的VID和Title组合的键值对列表
    Args:
        space_name: 空间名称
    Returns:
        vid_title_dict_list: VID和Title组合的键值对列表
    """
    vod_service = VodService()
    
    #设置认证信息
    ak = os.getenv('BYTEPLUS_AK')
    sk = os.getenv('BYTEPLUS_SK')

    if ak and sk:
        vod_service.set_ak(ak)
        vod_service.set_sk(sk)
    
    vid_title_dict_list = []
    try:
        req = VodGetMediaListRequest()
        req.SpaceName = space_name
        req.Status = 'Published'
        resp = vod_service.get_media_list(req)
        # print(resp)

        if resp.ResponseMetadata.Error.Code == '':
            
            mediaList = resp.Result.MediaInfoList
            for media in mediaList:
                vid = media.BasicInfo.Vid
                title = media.BasicInfo.Title
                print(f"VID: {vid}, Title: {title}")
                vid_title_dict_list.append({'VID': vid, 'Title': title})
    
        else:
            print(f"Error: {resp.ResponseMetadata.Error}")
            return []
            
        return vid_title_dict_list
    
    except Exception as e:
        print(f"Failed to get media list: {str(e)}")
        return []