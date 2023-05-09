from fpdf import FPDF
import gtts
from tika import parser
from moviepy.editor import *

from config.settings import BASE_DIR


def convert_from_txt_to_pdf(file_text, user_id, file_name, ):
    path = (
            BASE_DIR / 'media' / f'user_{user_id}' /
            'original_txt' / f'{file_text}'
    )
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=15)
    with open(f'{path}', 'r') as f:
        for i in f:
            pdf.cell(200, 10, txt=i, ln=1, align='C')

    path_pdf = (BASE_DIR / 'media' / f'user_{user_id}' / 'pdf_files')
    if not os.path.exists(path_pdf):
        os.makedirs(BASE_DIR / 'media' / f'user_{user_id}' / 'pdf_files')
    path_pdf = path_pdf.joinpath(f'{file_name}.pdf')
    pdf.output(path_pdf)


def convert_from_pdf_to_audio(pdf_file, user_id, file_name):
    path = (
            BASE_DIR / 'media' / f'user_{user_id}' /
            'original_pdf' / f'{pdf_file}'
    )
    pdf = parser.from_file(str(path))

    path_audio = (BASE_DIR / 'media' / f'user_{user_id}' / 'audio_files')
    if not os.path.exists(path_audio):
        os.makedirs(BASE_DIR / 'media' / f'user_{user_id}' / 'audio_files')
    path_audio = path_audio.joinpath(f'{file_name}.mp3')
    tts = gtts.gTTS(pdf['content'], lang='en')

    tts.save(path_audio)


def convert_from_video_to_gif(video_file, user_id, file_name, start, stop, ):
    path = (
            BASE_DIR / 'media' / f'user_{user_id}' /
            'original_video' / f'{video_file}'
    )

    gif = (VideoFileClip(f'{path}').subclip(int(start), int(stop)).resize(0.5))

    path_gif = (BASE_DIR / 'media' / f'user_{user_id}' / 'gif_files')

    if not os.path.exists(path_gif):
        os.makedirs(BASE_DIR / 'media' / f'user_{user_id}' / 'gif_files')
    path_gif = path_gif.joinpath(f'{file_name}.gif')
    gif.write_gif(f'{path_gif}')
