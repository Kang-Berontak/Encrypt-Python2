# Encrypt By : Ganz-XD
# Github     : https://github.com/Kang-Berontak
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzNV01QG8kVfiMhEOLfxpYN9nrAayNskBACYdgtb4J/SMq1Xpf2YEe2i0jqBgY0M8r0qACHHFLec6455ZpKLtlDqlI555ZLDqnKJTdfcttDTqmtStXmvTc9YmQZx8kC64EZvdf9/r6ve7qna6CvLry/h7f6fQpA4L8BdYBySzagbIRyDMqxUI5DOR7KXVDuCuUElBOh3A3l7lDugXIPCIyQBIG+vSDQKwUC7ftAoGU/CLQZAJGEL7CAQRC9LAyBSEF5GEQflEdAAmyfAdEPLw0wtDIQKMOw9gM5CHIkUM+CxCSDkJZJSIsh/E1BGnvKoyBHQQzDTgzUNyyPkOx9zT5YwJlOn3Og+8529p0HyopQRlk3ZBrkOaph+wK8RAAXQY6BvAjiHIjz8BLBj4Psgu1LIMfJrHwZ5AcgL7N8BQS6X8EMFyBdNoGCnQdxEV4idRMgJ2B7EqQZQETlKqUwZAy2PwQxFjQPMvJxXU1bFyK4FFS+hmGRrwF8OH9IEguXmZGRGMkfMCNfxU6MkThsXyNSyHwcxBXiIi3M08P8px7COcGYE3GSJxnzq/hJYr4ewXz1eDB/+O6Y/9JNOK8x5q8Z83XG/Leuk8Q8FcE8derj/PcE4cww5q+6SJ5mzH9OnBjmBGxnIphvnDrmfzDOm4z5FeOfYcwr3W/DTAv1LC3U9hiUxzD4mEb2XyrAhE1OmOWEJZ5kOU4oek5rSZ0Ol9Rppv1GOAo3WL0ZLjg3WZ0BMQdyFuQMqWmRP72hecCv3TwzdcBLUIGZ+kXyfWLqeoSphe+IqQneiBaZqV/zBlVkpv7Y+z4xNRVhauk7Yupf/BFzi9n5MnUqy9p0+EKF1Ihl4iUtVk4PNn9Xfp75CD9erW/weqh6UBx/mv+okLcP5fmIXIjICxG5GJGX7JqBcgzvbrzv0LfxDj7278Dex3DAWdN3n8/Bzwzw8QMUKYrBgcGVaj3O8HycPAn65KWenwzC48fOBHT53eD3wEYMdlLgbYBhGD5/EZORY8ATXIU/z9BH+UNFZaQ2//3bf/710+qjT1QfNbpOZce3NiYmJjK9qPtxKm9f+VSq8oXb9P0Eirue5UuWNupNteVTQN+ygyZVl7Lhj6D0QO5X3Yonfuj40vOaDR9rAbj32f17nud6HNxrOhniwjc4Az1rGTo48ENRl9j0ezmsu9vwLMfvJ2WQuo24MWIMGwPGudhZo0VrPKSVHt+G0z54zHTFI3T9dPR3a69efPFJhhgpUREl6ihR4hIZloiLEvHAuEpUeikVAmpD1RdFtbeXJjXJuAJU6jdomOJZs2jPvtsVmh+Ypp6qpmmu42WGV1RmRXuY5kEq6pXDzhzZkjcq5jNU2PcAHwctt0OvJZuccmzL3iZ7YkPO1PHe6JUjM/Rbzz1jAY2frc8ETkHyNi/zMF37xXHMQ4NFbXDwf3GYt2+b+q3+ftPfcr1DalbCjrWK82L2yd2w47ZuNh9UnM3ZVem5jl/ZMVvxwu77lZqsuu5OGHEl7NjQHdmaa+co+JO7D62tVVepjprWLH+rWX1DTZvcwRHayvhfSQjtn4Zs33Nq3n7DNxv7yIYzH3L8PCBZ/SqcrMtL9lP+Ldhzed3w3NTeusP8tOKprUq9w2H+dQdT96xWlCwudNgXjkpA9oX5DvuFt8XPFzvsF4+yL9etaod18SjrR/uBFA4gN9U6/JeO8td06dGe0UNNNbzWdARNt44l8Bv4XD6WwJ3E5+feRvw7gM7bc5EQe5afUjnaD8TmrNuQjrnl+w21ksvt7u5mj37teEOr1SWCuaZ3cIwcFnlT689NnemRVbe2FG0D5m2TN7O8T4v9XF7RFpC6b9Wl+bBiSzWM6mdNv9H0zcNG2tQ0WsvZNLPZrK+3CtpU5J6sKQuFqy1KVvfxvdeLUOqqqdcEulZaAI9cDyy7gZuwaes3kcJntJKtuxWhMrxRTU8zkF2LvwXSkRJdx7zj2o269KXAWtXZN2DCQth9PuBhXtWPHUA1GH2uP5Cz1eKCkDVXyMwUj8aUBlEIqiicUBX4frRVUZhvVXGBhv8I4ri0haC0hRMqDd+wttLyxbA0zr4YZF9Um8ee/QUtlJybJLJreFIpnbgYJC5mSPHpK5kMcPZw71LQu6R+eVLTfoaKmolOofZXgGsmqnTVHRNsUtESMTk9rafYraDkW+9fya3ZOMmFLgeFLr9/hbbm5iSXmJ9TPz+RWdlW2jsMdJce6EyW5iqV5qrgCMDnHzoRBF48jzVWXropOJ99qpZTUTULdyNUGvvr0cle4ucaP3/Ez1V+3uHn4xIdF0p0+OGQdXfT5ZTBfhWc0PCkJm0+LXmV3XXLwaWY09oVy7Gl02TPDUzIJxLWaDNkwZMVwcbUT62ly+G5rMLboGjajeCEZmuHhsfHG26r8lPwQUjvmq6SfBDigpBI6RCRgVaYj2r5otaSegGgIWCGVSX4qQY/teBHBAdT3zs8VLWdrCjMx7YrmnV5m0pVdEj7sdF9+Bfr7evtIWkA/xJGyrhkXMD7kjFonMG/IaMfpSHsS+E9iPeIkYxYDJ167zC2kJ58rU76G31LvG9n0x+pq7Oy/wBCwspL"))))