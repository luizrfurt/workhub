from tests.conftest import auth_header, create_collaborator, register_admin


def _general(listed: list[dict]) -> dict:
    match = next((item for item in listed if item.get("is_general")), None)
    assert match is not None, listed
    return match


def test_admin_and_collaborator_see_general_channel(client, unique):
    admin = register_admin(client, unique)
    collab = create_collaborator(client, admin["access_token"], unique)

    admin_list = client.get("/projects", headers=auth_header(admin["access_token"]))
    assert admin_list.status_code == 200, admin_list.text
    general = _general(admin_list.json())
    assert general["name"] == "Geral"
    assert admin_list.json()[0]["id"] == general["id"]

    collab_list = client.get("/projects", headers=auth_header(collab["access_token"]))
    assert collab_list.status_code == 200, collab_list.text
    collab_general = _general(collab_list.json())
    assert collab_general["id"] == general["id"]
    assert collab_general["member_count"] >= 2


def test_cannot_delete_or_edit_general_or_manage_members(client, unique):
    admin = register_admin(client, unique)
    collab = create_collaborator(client, admin["access_token"], unique)
    headers = auth_header(admin["access_token"])
    general = _general(client.get("/projects", headers=headers).json())

    deleted = client.delete(f"/projects/{general['id']}", headers=headers)
    assert deleted.status_code == 409

    renamed = client.patch(
        f"/projects/{general['id']}",
        json={"name": "Outro"},
        headers=headers,
    )
    assert renamed.status_code == 409

    added = client.post(
        f"/projects/{general['id']}/members",
        json={"user_id": collab["user"]["id"]},
        headers=headers,
    )
    assert added.status_code == 409

    removed = client.delete(
        f"/projects/{general['id']}/members/{collab['user']['id']}",
        headers=headers,
    )
    assert removed.status_code == 409


def test_cannot_create_task_on_general(client, unique):
    admin = register_admin(client, unique)
    collab = create_collaborator(client, admin["access_token"], unique)
    headers = auth_header(admin["access_token"])
    general = _general(client.get("/projects", headers=headers).json())

    created = client.post(
        f"/projects/{general['id']}/tasks",
        json={"title": "Não deve", "assigned_user_id": collab["user"]["id"]},
        headers=headers,
    )
    assert created.status_code == 403

    listed = client.get(f"/projects/{general['id']}/tasks", headers=headers)
    assert listed.status_code == 403
