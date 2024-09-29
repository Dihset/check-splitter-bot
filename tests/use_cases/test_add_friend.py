import uuid

import pytest

from src.domain.entities.user import User
from src.domain.services.user import IFriendService, IUserService
from src.domain.use_cases.user import AddFriendCommand, AddFriendsUseCase


@pytest.fixture
async def use_case(container) -> AddFriendsUseCase:
    return container.resolve(AddFriendsUseCase)


@pytest.fixture
async def friend_service(container) -> IFriendService:
    return container.resolve(IFriendService)


@pytest.fixture
async def first_user(container) -> User:
    user_service: IUserService = container.resolve(IUserService)
    return await user_service.get_or_create(User(oid=uuid.uuid4(), username="SomeName"))


async def test_base_add_friend(
    use_case: AddFriendsUseCase,
    friend_service: IFriendService,
    first_user: User,
):
    user = first_user
    user_friend = User(username="SomeName2")
    command = AddFriendCommand(
        user=user,
        friend=user_friend,
    )
    await use_case.execute(command)

    friens = await friend_service.get_friends(user_oid=user.oid)
    assert any(friend.username == user_friend.username for friend in friens)
