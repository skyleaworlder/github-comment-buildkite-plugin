# github-comment-buildkite-plugin

:speech_balloon: Post a comment to an Issue or PR on GitHub.

## Usage

### 1. Properties

| Name | Description |
| :-: | :-: |
| repository | owner and repo name, e.g. FluxML/Flux.jl |
| issue_number | PR id or Issue id |

### 2. Necessary Resources

* You have to provide an artifact named "comment.txt", in the same build.
* You have to provide 3 environment variables so that this plugin is able to generate `Installation Access Token` via GitHub REST-ful APIs:
  * `APP_ID`: any GitHub App should own an "id", required to generate Installation Access Token.
  * `INSTALLATION_ID`: any App installed should have an "installation id", required to generate Installation Access Token.
  * `PEM_CONTENT_B64`: related to the **private key**, but encoded in base64, also required to generate Installation Access Token.

### 3. Example

```yaml
steps:
  - label: ":rocket: Test plugin"
    env:
      APP_ID: 123456
      INSTALLATION_ID: 12345678
      PEM_CONTENT_B64: "ABCDEFGHIJKLMNOPQRSTUVWXYZ="
    commands: |
      echo "Hi! I'm github-comment-buildkite-plugin created by skyleaworlder!" > comment.txt
      buildkite-agent artifact upload comment.txt
    plugins:
      - skyleaworlder/github-comment:
          repository: Eternal-Night-Archer/BenchmarkData
          issue_number: 2
```
