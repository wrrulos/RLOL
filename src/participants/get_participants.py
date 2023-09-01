import requests
import os
import base64

from psutil import process_iter


class GetParticipants:
    @staticmethod
    def get_participants():
        """
        Get the names of participants in the League of Legends champion select screen.

        Returns:
            list or None: A list of participant names if successfully retrieved, or None if not.
        """
        
        client_port, client_token = GetParticipants.__get_league_client_info()

        if client_port and client_token:
            participants = GetParticipants.__get_champ_select_participants(client_port, client_token)
            return participants
        
        else:
            return None

    @staticmethod
    def __get_champ_select_participants(port, token):
        """
        Retrieves the names of participants in the League of Legends champion select.

        Parameters:
            port (str): The port number of the League of Legends client.
            token (str): The token used for authorization.

        Returns:
            list: A list of participant names in the champion select, or an empty list if retrieval fails.
        """

        url = f'https://127.0.0.1:{port}/chat/v5/participants/champ-select'
    
        headers = {
            'Authorization': f"Basic {base64.b64encode(f'riot:{token}'.encode()).decode()}",
            'Accept': 'application/json'
        }

        response = requests.get(url, headers=headers, verify=os.path.join(os.getcwd(), './src/participants/riotgames.pem'))

        if response.status_code == 200:
            data = response.json()
            participants = data['participants']
            participant_names = [participant['name'] for participant in participants]
            return participant_names
        
        else:
            return []
        
    @staticmethod
    def __get_league_client_info():
        """
        Retrieves information about the League of Legends client.

        Returns:
            tuple or None: A tuple containing the client port and token, or None if the client is not found.
        """
            
        league_processes = [proc for proc in process_iter() if proc.name() == 'LeagueClient.exe']

        if not league_processes:
            return None, None

        league_process = league_processes[0]
        client_port = league_process.cmdline()[2].split('=')[1]
        client_token = league_process.cmdline()[1].split('=')[1]
        return client_port, client_token