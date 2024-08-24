import ffmpeg

# Caminho para o vídeo de entrada
input_video = r'C:\Users\Anderson\Videos\tiktok\etb.mp4'

# Caminho para o vídeo de saída (incluindo a extensão .mp4)
output_video = r'C:\Users\Anderson\Videos\tiktok\etb1.mp4'

# Especificando o caminho completo para o executável ffmpeg
ffmpeg_path = r'C:\Users\Anderson\Downloads\ffmpeg-7.0.1-essentials_build\ffmpeg-7.0.1-essentials_build\bin\ffmpeg.exe'

try:
    # Aumentando a resolução para 1080x1920, ajustando a saturação e definindo o bitrate
    ffmpeg.input(input_video).output(
        output_video,
        vf='scale=1080:1920,eq=contrast=1.2:brightness=0.05:saturation=1.5,unsharp=7:7:1.0,hqdn3d',
        video_bitrate='9000k'
    ).run(cmd=ffmpeg_path)
    
    print("Processamento concluído. Novo vídeo salvo em:", output_video)
except ffmpeg.Error as e:
    print('Erro ao processar o vídeo:', e)
    print('Saída padrão:', e.stdout.decode('utf-8'))
    print('Saída de erro:', e.stderr.decode('utf-8'))



## ADICIONAR A QUALIDADE EM SCALE DE HD, FULLHD E 4K 
#try:
    # Aumentando a resolução para 1080x1920, ajustando a saturação e definindo o bitrate
  #  ffmpeg.input(input_video).output(
   #     output_video,
   #     vf='scale=1080:1920,eq=contrast=1.2:brightness=0.05:saturation=1.5,unsharp=7:7:1.0,hqdn3d',
   #     video_bitrate='9000k'
   # ).run(cmd=ffmpeg_path)
    
  #  print("Processamento concluído. Novo vídeo salvo em:", output_video)