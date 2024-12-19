import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template
from identity.flask import Auth
import app_config

load_dotenv(dotenv_path="./frontend/.env")

__version__ = "0.9.0"  # The version of this sample, for troubleshooting purpose


app = Flask(__name__)
app.config.from_object(app_config)

# https://identity-library.readthedocs.io/en/latest/flask.html
auth = Auth(
    app,
    authority=os.getenv("AUTHORITY"),
    client_id=os.getenv("CLIENT_ID"),
    client_credential=os.getenv("CLIENT_SECRET"),
    redirect_uri=os.getenv("REDIRECT_URI"),
    oidc_authority=os.getenv("OIDC_AUTHORITY"),
    b2c_tenant_name=os.getenv("B2C_TENANT_NAME"),
    b2c_signup_signin_user_flow=os.getenv("SIGNUPSIGNIN_USER_FLOW"),
    b2c_edit_profile_user_flow=os.getenv("EDITPROFILE_USER_FLOW"),
    b2c_reset_password_user_flow=os.getenv("RESETPASSWORD_USER_FLOW"),
)


def get_organization_name(context):
    api_result = (
        requests.get(  # Use access token to call a web api
            os.getenv("ENDPOINT03"),
            headers={"Authorization": "Bearer " + context["access_token"]},
            params={"belong": context["user"]["extension_ds_organization"]},
            timeout=30,
        ).json()
        if context.get("access_token")
        else "Did you forget to set the SCOPE environment variable?"
    )
    return api_result["organ_name"]


@app.route("/")
# @auth.login_required
@auth.login_required(scopes=os.getenv("SCOPE", "").split())
def index(*, context):
    # print(context)
    organ_name = get_organization_name(context)

    return render_template(
        "index.html",
        organ_name=organ_name,
        user=context["user"],
        edit_profile_url=auth.get_edit_profile_url(),
        api_endpoint_01=os.getenv("ENDPOINT01"),
        api_endpoint_02=os.getenv("ENDPOINT02"),
        # title=f"Flask Web App Sample v{__version__}",
        title=f"Flask+ADB2C+FastAPI Sample App",
    )


@app.route("/call_api_user_info")
@auth.login_required(scopes=os.getenv("SCOPE", "").split())
def call_downstream_api(*, context):
    api_result = (
        requests.get(  # Use access token to call a web api
            os.getenv("ENDPOINT01"),
            headers={"Authorization": "Bearer " + context["access_token"]},
            timeout=30,
        ).json()
        if context.get("access_token")
        else "Did you forget to set the SCOPE environment variable?"
    )
    return render_template("display.html", title="API Response", result=api_result)


@app.route("/call_api_get_members")
@auth.login_required(scopes=os.getenv("SCOPE", "").split())
def call_downstream_api2(*, context):
    api_result = (
        requests.get(  # Use access token to call a web api
            os.getenv("ENDPOINT02"),
            headers={"Authorization": "Bearer " + context["access_token"]},
            params={"belong": context["user"]["extension_ds_organization"]},
            timeout=30,
        ).json()
        if context.get("access_token")
        else "Did you forget to set the SCOPE environment variable?"
    )
    return render_template("display.html", title="API Response", result=api_result)


if __name__ == ("__main__"):
    app.run(debug=True, host="0.0.0.0", port=5000)
