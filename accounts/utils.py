from accounts.jwt import generate_access_token
from accounts.models import SocialInfo, User


def process_for_social_login(social_type, social_res):
    social_id = social_res.get('id', None)
    error = social_res.get("error", None)
    if not social_id or error:
        return False, None
    social_info, _ = SocialInfo.objects.get_or_create(auth_id=social_id)
    user, _ = User.objects.get_or_create(social_info=social_info, social_type=social_type)
    return True, {'message': 'success', 'access_token': generate_access_token(user.id)}
