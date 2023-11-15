from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from io import BytesIO

from api.constants import SCOPES, SERVICE_ACCOUNT_FILE
from api.models import GoogleDoc


def create_google_doc(data, name):
    """Создает новый документ Google Docs с заданным текстовым содержимым и названием,
    и делает его доступным для просмотра всем пользователям с ссылкой."""
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.document'
    }
    fh = BytesIO(data.encode())
    media = MediaIoBaseUpload(fh, mimetype='text/plain')
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    make_document_public(service, file.get('id'))
    new_doc = GoogleDoc(document_id=file.get('id'), name=name)
    new_doc.save()
    
    return file.get('id')


def make_document_public(service, file_id):
    """Делает документ Google Docs доступным для всех пользователей по ссылке."""
    public_permission = {
        'type': 'anyone',
        'role': 'reader',  # Или 'writer', если вы хотите разрешить редактирование
    }
    service.permissions().create(
        fileId=file_id,
        body=public_permission,
        fields='id',
    ).execute()