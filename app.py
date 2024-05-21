import customtkinter as ctk
from pytube import YouTube

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")  # Modes: "System" (standard), "Dark", "Light", color theme: dark-blue

root = ctk.CTk()
root.title("Descargar MP3 de YouTube")
root.geometry("600x400")
root.resizable("800","1240")
root.iconbitmap("icon.ico")

def descargar_mp3():
    url = url_entry.get()
    name_file = name_entry.get() + '.mp3'
    
    try:
        # Descarga el video de YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download(filename='temp')

        # Convierte el video descargado a formato mp3
        clip = mp.AudioFileClip('temp.mp4')
        clip.write_audiofile(name_file)

        # Elimina el archivo de video temporal
        clip.close()
        os.remove('temp.mp4')

        messagebox.showinfo("Éxito", "El archivo se ha descargado y convertido a MP3 correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descargar o convertir el archivo: {str(e)}")

def limpiar_campos():
    url_entry.delete(0, ctk.END)
    destino_descarga.delete(0, ctk.END)
    mensaje_error.set("")
    mensaje_exito.set("")

frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label_url = ctk.CTkLabel(frame, text="URL del video:")
label_url.pack(pady=10, padx=20, fill="both")

url_entry = ctk.CTkEntry(frame, width=50)
url_entry.pack(pady=10, padx=40, fill="both")

button_download = ctk.CTkButton(master=frame, text="Descargar", command=descargar_mp3)
button_download.place(relx=0.5, rely=0.7, anchor="center")

name_level = ctk.CTkLabel(frame, text="Nombre del archivo:")
name_level.pack(pady=10, padx=40, fill="both")

name_entry = ctk.CTkEntry(frame, width=50)
name_entry.pack(pady=10, padx=40, fill="both")

boton_clear = ctk.CTkButton(master=frame, text="Limpiar", command=limpiar_campos)
boton_clear.place(relx=0.5, rely=0.8, anchor="center")






root.mainloop()