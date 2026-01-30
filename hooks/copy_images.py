import shutil
import os
import logging

log = logging.getLogger('mkdocs')

def on_pre_build(config):
    """构建前将图片复制到 site 目录，确保部署时包含"""
    src = os.path.join(config['docs_dir'], '图片')
    dst = os.path.join(config['site_dir'], '图片')
    
    if os.path.exists(src):
        # 确保目标目录存在
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        # 复制整个图片目录到构建输出
        shutil.copytree(src, dst, dirs_exist_ok=True)
        log.info(f"Copied images from {src} to {dst}")
    else:
        log.warning(f"Images directory not found: {src}")

def on_post_build(config):
    """构建后确认图片已复制"""
    dst = os.path.join(config['site_dir'], '图片')
    if os.path.exists(dst):
        count = len([f for f in os.listdir(dst) if os.path.isfile(os.path.join(dst, f))])
        log.info(f"Images in site: {count} files")