from kubiya_sdk.tools.models import Arg, Tool
from kubiya_sdk.tools.registry import tool_registry
from . import common

class BaseClearlyTool(Tool):
    def __init__(self, name: str, description: str, args: list[Arg], content: str):
        base_secrets = [
            "AKAMAI_ACCESS_TOKEN",
            "AKAMAI_CLIENT_SECRET", 
            "AKAMAI_CLIENT_TOKEN",
            "AKAMAI_HOST",
            "AWS_ACCESS_KEY_ID",
            "AWS_SECRET_ACCESS_KEY", 
            "AWS_SESSION_TOKEN",
            "CCI_LDAP_URL",
            "CCI_ADMIN_USER",
            "CCI_ADMIN_PASSWORD",
            "AAD_CONTROLTOWER_ROLEACCESS_SECRET",
            "AAD_PYTHON_AZUREAD_AWS_SECRET",
            "AWS_SSO_IDENTITY_STORE_ID",
            "AWS_SSO_IDENTITY_STORE_ARN",
            "AWS_PERMISSION_SET_ARN_READ_ONLY_ACCESS",
            "AWS_PERMISSION_SET_ARN_POWER_USER_ACCESS",
            "AWS_PERMISSION_SET_ARN_POWER_USER_PLUS_ACCESS", 
            "AWS_PERMISSION_SET_ARN_ADMINISTRATOR_ACCESS",
            "AWS_GLOBAL_GROUP_ID_POWER_USER",
            "AWS_GLOBAL_GROUP_ID_POWER_USER_PLUS",
            "TEAMS_INCOMING_HOOK_URL"
        ]
        
        super().__init__(
            name=name,
            type="docker",
            image="ttl.sh/clearly-gen3-testv3:latest",
            description=description,
            args=args,
            content=content,
            secrets=base_secrets,
            with_files=common.COMMON_FILES,
            env=common.COMMON_ENV
        )

# Help tool
help_tool = BaseClearlyTool(
    name="help",
    description="Display help information about available functions",
    args=[],
    content="""
python /app/clearly_actions.py help
""",
)

# Testing tools
direct_billing_network_creation_additions = BaseClearlyTool(
    name="direct_billing_network_creation_additions",
    description="Add additional network configurations for direct billing",
    args=[
        Arg(name="vpc_id", description="VPC ID"),
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale"),
        Arg(name="entity_environment", description="Entity environment"),
        Arg(name="gateway_id", description="Gateway ID")
    ],
    content="""
python /app/clearly_actions.py direct_billing_network_creation_additions {vpc_id} {entity_acronym} {entity_locale} {entity_environment} {gateway_id}
""",
)

# Akamai tools
test_akamai = BaseClearlyTool(
    name="test_akamai",
    description="Test Akamai connection",
    args=[],
    content="""
python /app/clearly_actions.py test_akamai
""",
)

create_zone = BaseClearlyTool(
    name="create_zone",
    description="Create DNS zone in Akamai",
    args=[
        Arg(name="zone", description="Zone name to create")
    ],
    content="""
python /app/clearly_actions.py create_zone {zone}
""",
)

create_dns_record = BaseClearlyTool(
    name="create_dns_record", 
    description="Create DNS record in Akamai",
    args=[
        Arg(name="zone", description="Zone name"),
        Arg(name="record_type", description="DNS record type"),
        Arg(name="record_name", description="DNS record name"),
        Arg(name="record_value", description="DNS record value"),
        Arg(name="ttl", description="TTL value")
    ],
    content="""
python /app/clearly_actions.py create_dns_record {zone} {record_type} {record_name} {record_value} {ttl}
""",
)

apply_zone_changelist = BaseClearlyTool(
    name="apply_zone_changelist",
    description="Apply zone changelist in Akamai",
    args=[
        Arg(name="zone", description="Zone name")
    ],
    content="""
python /app/clearly_actions.py apply_zone_changelist {zone}
""",
)

migrate_aws_zone_records_to_akamai = BaseClearlyTool(
    name="migrate_aws_zone_records_to_akamai",
    description="Migrate AWS zone records to Akamai",
    args=[
        Arg(name="zone", description="Zone name")
    ],
    content="""
python /app/clearly_actions.py migrate_aws_zone_records_to_akamai {zone}
""",
)

migrate_single_aws_zone_to_akamai = BaseClearlyTool(
    name="migrate_single_aws_zone_to_akamai",
    description="Migrate single AWS zone to Akamai",
    args=[
        Arg(name="zone", description="Zone name")
    ],
    content="""
python /app/clearly_actions.py migrate_single_aws_zone_to_akamai {zone}
""",
)

# Control Tower tools
add_roles_to_aws_account = BaseClearlyTool(
    name="add_roles_to_aws_account",
    description="Add roles to AWS account",
    args=[
        Arg(name="account_number", description="AWS account number"),
        Arg(name="group_name", description="Group name")
    ],
    content="""
python /app/clearly_actions.py add_roles_to_aws_account {account_number} {group_name}
""",
)

create_aws_account = BaseClearlyTool(
    name="create_aws_account",
    description="Create new AWS account",
    args=[
        Arg(name="ou_id", description="Organization Unit ID"),
        Arg(name="ou_name", description="Organization Unit name"),
        Arg(name="account_name", description="Account name"),
        Arg(name="account_email", description="Account email")
    ],
    content="""
python /app/clearly_actions.py create_aws_account {ou_id} {ou_name} {account_name} {account_email}
""",
)

migrate_control_tower = BaseClearlyTool(
    name="migrate_control_tower",
    description="Migrate control tower",
    args=[],
    content="""
python /app/clearly_actions.py migrate_control_tower
""",
)

add_esg_to_all_control_tower_accounts = BaseClearlyTool(
    name="add_esg_to_all_control_tower_accounts",
    description="Add ESG to all control tower accounts",
    args=[
        Arg(name="esg_name", description="ESG name"),
        Arg(name="permission_set_arn_secret_key", description="Permission set ARN secret key")
    ],
    content="""
python /app/clearly_actions.py add_esg_to_all_control_tower_accounts {esg_name} {permission_set_arn_secret_key}
""",
)

add_esg_to_list_of_control_tower_accounts = BaseClearlyTool(
    name="add_esg_to_list_of_control_tower_accounts",
    description="Add ESG to list of control tower accounts",
    args=[
        Arg(name="esg_name", description="ESG name"),
        Arg(name="permission_set_arn_secret_key", description="Permission set ARN secret key"),
        Arg(name="account_numbers", description="List of account numbers")
    ],
    content="""
python /app/clearly_actions.py add_esg_to_list_of_control_tower_accounts {esg_name} {permission_set_arn_secret_key} {account_numbers}
""",
)

add_esg_to_single_control_tower_account = BaseClearlyTool(
    name="add_esg_to_single_control_tower_account",
    description="Add ESG to single control tower account",
    args=[
        Arg(name="esg_name", description="ESG name"),
        Arg(name="permission_set_arn_secret_key", description="Permission set ARN secret key"),
        Arg(name="account_number", description="Account number")
    ],
    content="""
python /app/clearly_actions.py add_esg_to_single_control_tower_account {esg_name} {permission_set_arn_secret_key} {account_number}
""",
)

# Direct Billing AAD tools
add_login_name_to_control_tower_role = BaseClearlyTool(
    name="add_login_name_to_control_tower_role",
    description="Add login name to control tower role",
    args=[],
    content="""
python /app/clearly_actions.py add_login_name_to_control_tower_role
""",
)

add_to_control_tower_role = BaseClearlyTool(
    name="add_to_control_tower_role",
    description="Add to control tower role",
    args=[
        Arg(name="acronym", description="Entity acronym"),
        Arg(name="locale", description="Entity locale")
    ],
    content="""
python /app/clearly_actions.py add_to_control_tower_role {acronym} {locale}
""",
)

# Direct Billing Account Access tools
add_default_roles = BaseClearlyTool(
    name="add_default_roles",
    description="Add default roles to account",
    args=[
        Arg(name="account", description="Account number")
    ],
    content="""
python /app/clearly_actions.py add_default_roles {account}
""",
)

add_granular_group_access_roles = BaseClearlyTool(
    name="add_granular_group_access_roles",
    description="Add granular group access roles",
    args=[
        Arg(name="account", description="Account number"),
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale"),
        Arg(name="env", description="Environment")
    ],
    content="""
python /app/clearly_actions.py add_granular_group_access_roles {account} {entity_acronym} {entity_locale} {env}
""",
)

find_group_id = BaseClearlyTool(
    name="find_group_id",
    description="Find group ID",
    args=[
        Arg(name="groupname", description="Group name")
    ],
    content="""
python /app/clearly_actions.py find_group_id {groupname}
""",
)

# Direct Billing Control Tower tools
create_organizational_unit = BaseClearlyTool(
    name="create_organizational_unit",
    description="Creates organizational unit in the Direct Billing Brands OU",
    args=[
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale")
    ],
    content="""
python /app/clearly_actions.py create_organizational_unit {entity_acronym} {entity_locale}
""",
)

direct_billing_account_creation = BaseClearlyTool(
    name="direct_billing_account_creation",
    description="Creates 4 accounts based on supplied acronym and locale",
    args=[
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale"),
        Arg(name="ou_id", description="Organization Unit ID")
    ],
    content="""
python /app/clearly_actions.py direct_billing_account_creation {entity_acronym} {entity_locale} {ou_id}
""",
)

direct_billing_single_account_creation = BaseClearlyTool(
    name="direct_billing_single_account_creation",
    description="Create single account for direct billing",
    args=[
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale"),
        Arg(name="ou_id", description="Organization Unit ID"),
        Arg(name="env", description="Environment")
    ],
    content="""
python /app/clearly_actions.py direct_billing_single_account_creation {entity_acronym} {entity_locale} {ou_id} {env}
""",
)

direct_billing_network_creation = BaseClearlyTool(
    name="direct_billing_network_creation",
    description="Create network for direct billing",
    args=[
        Arg(name="network_address", description="Network address"),
        Arg(name="account_number", description="Account number"),
        Arg(name="account_region", description="Account region"),
        Arg(name="entity_acronym", description="Entity acronym"),
        Arg(name="entity_locale", description="Entity locale"),
        Arg(name="entity_environment", description="Entity environment")
    ],
    content="""
python /app/clearly_actions.py direct_billing_network_creation {network_address} {account_number} {account_region} {entity_acronym} {entity_locale} {entity_environment}
""",
)

# General tools
send_teams_message = BaseClearlyTool(
    name="send_teams_message",
    description="Send message to Teams channel",
    args=[
        Arg(name="message", description="Message to send")
    ],
    content="""
python /app/clearly_actions.py send_teams_message {message}
""",
)

create_security_group = BaseClearlyTool(
    name="create_security_group",
    description="Create security group",
    args=[
        Arg(name="group_name", description="Group name"),
        Arg(name="group_description", description="Group description")
    ],
    content="""
python /app/clearly_actions.py create_security_group {group_name} {group_description}
""",
)

get_entra_application_json = BaseClearlyTool(
    name="get_entra_application_json",
    description="Get Entra application JSON",
    args=[
        Arg(name="app_id", description="Application ID")
    ],
    content="""
python /app/clearly_actions.py get_entra_application_json {app_id}
""",
)

add_devs_to_group = BaseClearlyTool(
    name="add_devs_to_group",
    description="Add developers to group",
    args=[
        Arg(name="group_id", description="Group ID")
    ],
    content="""
python /app/clearly_actions.py add_devs_to_group {group_id}
""",
)

find_members_of_ldap_groupname = BaseClearlyTool(
    name="find_members_of_ldap_groupname",
    description="Find members of LDAP group",
    args=[
        Arg(name="group_name", description="Group name"),
        Arg(name="search_base", description="Search base")
    ],
    content="""
python /app/clearly_actions.py find_members_of_ldap_groupname {group_name} {search_base}
""",
)

test_ldap_connection = BaseClearlyTool(
    name="test_ldap_connection",
    description="Test LDAP connection",
    args=[],
    content="""
python /app/clearly_actions.py test_ldap_connection
""",
)

# Workspaces tools
sync_workspaces_with_ad = BaseClearlyTool(
    name="sync_workspaces_with_ad",
    description="Sync workspaces with AD",
    args=[],
    content="""
python /app/clearly_actions.py sync_workspaces_with_ad
""",
)

sync_billing_group_workspaces = BaseClearlyTool(
    name="sync_billing_group_workspaces",
    description="Sync billing group workspaces",
    args=[],
    content="""
python /app/clearly_actions.py sync_billing_group_workspaces
""",
)

get_created_workspaces_names = BaseClearlyTool(
    name="get_created_workspaces_names",
    description="Get created workspaces names for directory",
    args=[
        Arg(name="directory_id", description="Directory ID")
    ],
    content="""
python /app/clearly_actions.py get_created_workspaces_names_for_directory {directory_id}
""",
)

power_on_stopped_workspaces = BaseClearlyTool(
    name="power_on_stopped_workspaces",
    description="Power on stopped workspaces for directory",
    args=[
        Arg(name="directory_id", description="Directory ID")
    ],
    content="""
python /app/clearly_actions.py power_on_stopped_workspaces {directory_id}
""",
)

# Register all tools
tools = [
    help_tool,
    direct_billing_network_creation_additions,
    # Akamai tools
    test_akamai,
    create_zone,
    create_dns_record,
    apply_zone_changelist,
    migrate_aws_zone_records_to_akamai,
    migrate_single_aws_zone_to_akamai,
    # Control Tower tools
    add_roles_to_aws_account,
    create_aws_account,
    migrate_control_tower,
    add_esg_to_all_control_tower_accounts,
    add_esg_to_list_of_control_tower_accounts,
    add_esg_to_single_control_tower_account,
    # Direct Billing AAD tools
    add_login_name_to_control_tower_role,
    add_to_control_tower_role,
    # Direct Billing Account Access tools
    add_default_roles,
    add_granular_group_access_roles,
    find_group_id,
    # Direct Billing Control Tower tools
    create_organizational_unit,
    direct_billing_account_creation,
    direct_billing_single_account_creation,
    direct_billing_network_creation,
    # General tools
    send_teams_message,
    create_security_group,
    get_entra_application_json,
    add_devs_to_group,
    find_members_of_ldap_groupname,
    test_ldap_connection,
    # Workspaces tools
    sync_workspaces_with_ad,
    sync_billing_group_workspaces,
    get_created_workspaces_names,
    power_on_stopped_workspaces
]

# Register each tool individually under the "clearly" namespace
for tool in tools:
    tool_registry.register("clearly", tool)
