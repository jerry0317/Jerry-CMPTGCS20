import requests

def lastCommit():
    query = '''
    query ($owner: String!, $name: String!) {
      repository(owner: $owner, name: $name) {
        url
        sshUrl
        updatedAt
      	ref(qualifiedName: "master"){
          target {
            ... on Commit {
              history(first: 10) {
                pageInfo {
                  hasNextPage
                }
                nodes{
                  messageHeadline
                  messageHeadlineHTML
                  messageBody
                  messageBodyHTML
                  url
                  oid
                  author {
                    date
                    email
                    name
                  }
                  pushedDate
                }
              }
            }
          }
        }
      }
    }
    '''

    variables = {
        "owner": "jerry0317",
        "name": "Jerry-CMPTGCS20"
    }
    api_token = str(open('token.key','r').read().splitlines()[0])
    headers = {'Authorization': 'token %s' % api_token}

    request = requests.post('https://api.github.com/graphql', json={"query": query, "variables": variables}, headers=headers)

    if request.status_code == 200:
        pass
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    return request.json()['data']['repository']['ref']['target']['history']['nodes'][0]
