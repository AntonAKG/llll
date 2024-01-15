from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from github import Github

router = Router()

github = Github('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')


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply('Hello')


@router.message(F.text=='da')
async def cmd_msg(message: Message):
    organization_name = "AntonAKG"
    organization = github.get_organization(organization_name)

    for repo in organization.get_repos():
        pull_requests = repo.get_pulls(state='all', sort='created', direction='desc', head=repo.default_branch)
        latest_pull_request = next(pull_requests, None)

        if latest_pull_request:
            # telegram_bot.send_message(chat_id=telegram_chat_id,
            #                           text=f"New pull request in {repo.full_name}: {latest_pull_request.html_url}")
            await message.answer(f"New pull request in {repo.full_name}: {latest_pull_request.html_url}")
