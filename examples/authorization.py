import natch


@natch.pattern(
    natch.Any(),
    natch.Partial(
        user=natch.Partial(
            is_authenticated=True,
        ),
    ),
)
def get_user_profile(user_id, request):
    profile = dict()
    return profile


@natch.any()
def get_user_profile(user_id, request):
    raise Exception('Not authenticated.')
