import PropTypes from 'prop-types';
import React from 'react'
import { render } from 'react-dom';
import Thumbnail from './thumbnail'
import CreatePage from './create';
import Page from './page';

class Homepage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      logname: "",
      blownUpThumbnail: 0,
      thumbnails: []
    };
  }

  componentDidMount() {
    // fetch all the thumbnails, set state
    fetch("/api/v1/page/fetchall/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
        console.log(data);
        this.setState({ logname: data.logname, thumbnails: data.pages });
      })
      .catch((error) => console.log(error));
  }

  // Hook passed to CreatePage component.
  // Appends a thumbnail to the pages array after it was created
  // The request to create a new thumbnail is handled in the CreatePage component.
  addThumbnail(page) {
    const { thumbnails } = this.state;
    thumbnails.push(page);
    this.setState({ thumbnails });
  }
  
  // Hook passed to Thumbnail component.
  // Sets the "blownUpThumbnail" state variable to the thumbnail that was clicked
  // invokes render() due to setState() invocation, which then renders the thumbnail
  // as a center stage Page component
  thumbnailBlowUp(pageId) {
    this.setState({ blownUpThumbnail: pageId });
  }

  render() {
    const {
      logname,
      thumbnails,
      blownUpThumbnail
    } = this.state;
    var loggedIn = true;
    if (logname === null) {
      loggedIn = false;
    }
    return (
      <div className="wrapper">
        {
          thumbnails.map((page) => (
            <Thumbnail
              pageId={page.pageId}
              title={page.title}
              description={page.description}
              pageSize={page.pageSize}
              thumbnailBlowUp={this.thumbnailBlowUp.bind(this)}
            />
          ))
        }
        {
          loggedIn ? (<CreatePage addThumbnail={this.addThumbnail.bind(this)}/>) : (null)
        }
        {
          blownUpThumbnail === 0 ? (null) : (
            <Page title="Mocked Title" description="Mocked Description" />
          )
        }
      </div>
    );
  }
}

Homepage.propTypes = {
  // prop types go here
  // s: PropTypes.string.isRequired,
  thumbnails: PropTypes.instanceOf(Array)
};

render(
  <div>
    <Homepage />
  </div>,
  document.getElementById('reactEntry'),
);