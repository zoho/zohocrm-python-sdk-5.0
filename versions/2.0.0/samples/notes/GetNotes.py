from datetime import datetime
from zohocrmsdk.src.com.zoho.api.authenticator import OAuthToken
from zohocrmsdk.src.com.zoho.crm.api import Initializer, ParameterMap, HeaderMap
from zohocrmsdk.src.com.zoho.crm.api.dc import USDataCenter
from zohocrmsdk.src.com.zoho.crm.api.notes import NotesOperations, GetNotesParam, GetNotesHeader, ResponseWrapper, \
    APIException


class GetNotes:
    @staticmethod
    def initialize():
        environment = USDataCenter.PRODUCTION()
        token = OAuthToken(client_id="clientID", client_secret="clientSecret", grant_token="grantToken")
        Initializer.initialize(environment, token)

    @staticmethod
    def get_notes():
        """
        This method is used to get the list of notes and print the response.
        """
        notes_operations = NotesOperations()
        param_instance = ParameterMap()
        param_instance.add(GetNotesParam.page, "1")
        param_instance.add(GetNotesParam.per_page, "200")
        param_instance.add(GetNotesParam.fields, "id")
        header_instance = HeaderMap()
        header_instance.add(GetNotesHeader.if_modified_since, str(datetime.fromisoformat('2019-06-01T00:00:00+05:30')))
        response = notes_operations.get_notes(param_instance, header_instance)
        if response is not None:
            print('Status Code: ' + str(response.get_status_code()))
            if response.get_status_code() in [204, 304]:
                print('No Content' if response.get_status_code() == 204 else 'Not Modified')
                return
            response_object = response.get_object()
            if response_object is not None:
                if isinstance(response_object, ResponseWrapper):
                    notes_list = response_object.get_data()
                    for note in notes_list:
                        print("Note Id: " + str(note.get_id()))
                        print("Note NoteTitle: " + str(note.get_note_title()))
                        print("Note NoteContent: " + str(note.get_note_content()))
                        owner = note.get_owner()
                        if owner is not None:
                            print("Note Owner - Name: " + str(owner.get_name()))
                            print("Note Owner - ID: " + str(owner.get_id()))
                            print("Note Owner - Email: " + str(owner.get_email()))
                        if note.get_modified_time() is not None:
                            print("Note ModifiedTime: " + str(note.get_modified_time()))
                        attachments = note.get_attachments()
                        if attachments is not None:
                            for attachment in attachments:
                                GetNotes.print_attachment(attachment)
                        print("Note CreatedTime: " + str(note.get_created_time()))
                        parent_id = note.get_parent_id()
                        if parent_id is not None:
                            if parent_id.get_key_value('name') is not None:
                                print('Note parent record Name: ' + str(parent_id.get_key_value('name')))
                            print('Note parent record ID: ' + str(parent_id.get_id()))
                        print("Note Editable: " + str(note.get_editable()))
                        print("Note SeModule: " + str(note.get_se_module()))
                        print("Note IsSharedToClient: " + str(note.get_is_shared_to_client()))
                        modified_by = note.get_modified_by()
                        if modified_by is not None:
                            print("Note Modified By - Name: " + str(modified_by.get_name()))
                            print("Note Modified By - ID: " + str(modified_by.get_id()))
                            print("Note Modified By - Email: " + str(modified_by.get_email()))
                        print("Note Size: " + str(note.get_size()))
                        print("Note State: " + str(note.get_state()))
                        print("Note VoiceNote: " + str(note.get_voice_note()))
                        created_by = note.get_created_by()
                        if created_by is not None:
                            print("Note Created By - Name: " + created_by.get_name())
                            print("Note Created By - ID: " + str(created_by.get_id()))
                            print("Note Created By - Email: " + created_by.get_email())
                    info = response_object.get_info()
                    if info is not None:
                        if info.get_per_page() is not None:
                            print('Note Info PerPage: ' + str(info.get_per_page()))
                        if info.get_count() is not None:
                            print('Note Info Count: ' + str(info.get_count()))
                        if info.get_page() is not None:
                            print('Note Info Page: ' + str(info.get_page()))
                        if info.get_more_records() is not None:
                            print('Note Info MoreRecords: ' + str(info.get_more_records()))
                elif isinstance(response_object, APIException):
                    print("Status: " + response_object.get_status().get_value())
                    print("Code: " + response_object.get_code().get_value())
                    print("Details")
                    details = response_object.get_details()
                    for key, value in details.items():
                        print(key + ' : ' + str(value))
                    print("Message: " + response_object.get_message().get_value())

    @staticmethod
    def print_attachment(attachment):
        print('Attachment ID : ' + str(attachment.get_id()))
        owner = attachment.get_owner()
        if owner is not None:
            print("Attachment Owner - Name: " + owner.get_name())
            print("Attachment Owner - ID: " + str(owner.get_id()))
            print("Attachment Owner - Email: " + owner.get_email())
        print("Attachment Modified Time: " + str(attachment.get_modified_time()))
        print("Attachment File Name: " + str(attachment.get_file_name()))
        print("Attachment Created Time: " + str(attachment.get_created_time()))
        print("Attachment File Size: " + str(attachment.get_size()))
        parent_id = attachment.get_parent_id()
        if parent_id is not None:
            print("Attachment parent record Name: " + str(parent_id.get_key_value("name")))
            print("Attachment parent record ID: " + str(parent_id.get_id()))
        print("Attachment is Editable: " + str(attachment.get_editable()))
        print("Attachment File ID: " + str(attachment.get_file_id()))
        print("Attachment File Type: " + str(attachment.get_type()))
        print("Attachment seModule: " + str(attachment.get_se_module()))
        modified_by = attachment.get_modified_by()
        if modified_by is not None:
            print("Attachment Modified By - Name: " + modified_by.get_name())
            print("Attachment Modified By - ID: " + str(modified_by.get_id()))
            print("Attachment Modified By - Email: " + modified_by.get_email())
        print("Attachment State: " + attachment.get_state())
        created_by = attachment.get_created_by()
        if created_by is not None:
            print("Attachment Created By - Name: " + created_by.get_name())
            print("Attachment Created By - ID: " + str(created_by.get_id()))
            print("Attachment Created By - Email: " + created_by.get_email())
        print("Attachment LinkUrl: " + str(attachment.get_link_url()))


GetNotes.initialize()
GetNotes.get_notes()
