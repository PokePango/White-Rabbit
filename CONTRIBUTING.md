# Contributing

Thanks for contributing to the project! Before submitting a pull request,
please make sure you read through the following guidelines.

## Testing

### Github Actions

The repository currently has two Github Actions workflows in place. The first
tests dependency installation and linting, while the second tests that the bot
can log in. However, the latter is not run on pull requests, because it fails
without the access token. Pull requests that do not pass the first test will
not be accepted, as they break the bot.

### Manual Testing

Before submitting a pull request which changes the code, do a test run of
Alice is Missing as follows:

- Start the bot (for instructions on how to do so, see the documentation
  [here](https://white-rabbit.readthedocs.io/en/stable/user-guide/installation.html)).
- Add two more accounts to the server (in order for the bot to see enough
  players) and assign yourself and the others character roles. You can also do
  this with only one extra account by assigning a role to the bot. Make sure
  that you have the `Charlie` role and that your nickname is set to
  "Charlie Barnes".
- Run through a game by calling `!init`, `!setup_clues`, and `!start`.
  Manually assigning the 10 minute card is optional, as the bot will auto
  assign it to Charlie if the command is never called. You can leave this to
  run in the background, as it will take the full 90 minutes.
- Copy and paste the starting message for Charlie Barnes into the group chat
  channel, then go back to the bot channel and call `!pdf`. If this runs
  without errors, open the exported PDF file and make sure it matches the
  game.

If you've reached this point and nothing looks amiss, you're done! Submit the
pull request, and thanks again for the help.