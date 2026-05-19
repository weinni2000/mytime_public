def post_init_hook(env):
    env["res.country"].action_set_default_preferred_guest_registration()
