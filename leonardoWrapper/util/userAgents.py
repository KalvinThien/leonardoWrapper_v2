import sys
from user_agent import generate_user_agent

sys.dont_write_bytecode = True

def get_random_user_agent(os: str = 'random') -> str:
    """
    Generate a random user agent based on the specified OS.
    
    :param os: The operating system for which to generate the user agent.
               Options are 'linux', 'mac', 'windows', or 'random'.
    :return: A string representing the user agent.
    """
    if os == 'random':
        return generate_user_agent()
    elif os == 'linux':
        return generate_user_agent(os=('linux',))
    elif os == 'mac':
        return generate_user_agent(os=('mac',))
    elif os == 'windows':
        return generate_user_agent(os=('win',))
    else:
        raise ValueError("Invalid OS specified. Choose from 'linux', 'mac', 'windows', or 'random'.")

# Test the function
if __name__ == "__main__":
    print("Random User Agent:", get_random_user_agent('random'))
    #print("Linux User Agent:", get_random_user_agent('linux'))
    #print("Mac User Agent:", get_random_user_agent('mac'))
    #print("Windows User Agent:", get_random_user_agent('windows'))
