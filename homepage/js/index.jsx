import PropTypes from 'prop-types';
import { react } from 'react'
import Thumbnail from './thumbnail'

class Homepage extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pages: props.pages
    };
  }

  componentDidMount() {
    // fetch all the pages, set state
    fetch("/api/v1/page/fetchall/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        const { pages } = data;
        this.setState({ pages });
      })
      .catch((error) => console.log(error));
  }

  render() {
    const { pages } = this.state;
    return (
      <div>
        {
          pages.map((page) => (
            <Thumbnail 
              pageId={page.page_id}
              title={page.title}
              description={page.description}
              pageSize={page.card_size}
            />
          ))
        }
      </div>
    );
  }
}

Homepage.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
  pages: PropTypes.instanceOf(Array)
};

Homepage.defaultProps = {
  // default prop values go here if not required
  pages: []
};

render(
  <div>
    <Homepage />
  </div>,
  document.getElementById('reactEntry'),
);