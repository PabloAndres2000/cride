# Typing
from typing import Optional

# Providers
from cride.users.providers import users as user_providers


def get_plan_by_uuid(pk: int) -> Optional["users.User"]:
    return user_providers.get_user_by_pk(pk=pk)
